#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 13:07:27 2020

@author: ichraf ben fadhel
"""
# Import pandas 
import pandas as pd 
import os
import sys 
def fetch_bugzilla(issues_path,resultat):

  
    # reading csv file  
    data=pd.read_csv(issues_path) 

    #filter the data with this given features
    #status in (Resolved, Closed) ,resolution = Fixed 
    #component = core  , ORDER BY created DESC'
    #Note : some project don't have  Component=Core so it really depend on the project 
    filtred_data = data[(data.Component=='Core')&((data.Status=="RESOLVED")|(data.Status=="CLOSED"))&(data.Resolution=="FIXED")]
    
    # order by reverse the chronogical order 
    filtred_data = filtred_data.sort_values(by ='Opened',ascending=False) 
    # write this filtred data in file
    #check if directory issues exists else create (will contain the results)
    directory="issues"
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    file_result_path=os.path.join(directory, resultat+'.csv')   
    print(file_result_path)
    filtred_data.to_csv (file_result_path, sep="," , index=False)
    print("Done ! check issues directory you will find the resulted file")

#get the user input 
bugs_path= str(sys.argv[1])
output_file_name=str(sys.argv[2])
#run the file
fetch_bugzilla(bugs_path,output_file_name)
