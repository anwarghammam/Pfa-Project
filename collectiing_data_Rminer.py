# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:19:43 2020

@author: User
"""

import os
import time
import subprocess
import csv, json, sys
#give the path of the porject 
project=str(sys.argv[1])
#the path of the folder where the result will be stored
result=str(sys.argv[2])

tags=[]
#the tags of the releases will be stored in file
file = open(r"test.json", 'w')

list_files = subprocess.run(["git","tag"] ,stdout=file,shell=True)

#we stor all the releases tags in a list
with open(r"test.json") as file:
    
    for line in file: 
        
        
        tags.append(line)

# os.chdir(path of Refactoring rminer )		
os.chdir(r"C:\Users\User\Desktop\RefactoringMiner-1.0\bin")



#now for each release we take the current release and the rfollowing one and try to detect the refactoring that happened between them
for i in range(len(tags)) :

        
    
    tag1=str(tags[i].rstrip("\n"))
    tag2=str(tags[i+1].rstrip("\n"))
    print(tag1)
    print(tag2)
    print(i)
#	 the  refactoring that happned betweenn two releases will be  stroed in a json file : file_commits 
    file_commits = open(r"C:\Users\User\Desktop\jsontests\test"+str(i)+".json", 'w')
    list_files1 = subprocess.run(["RefactoringMiner", "-bt" ,r"C:\Users\User\Desktop\projects"+"\\"+project,tag1,tag2],stdout=file_commits,shell=True)
    
    #somme tags contain an \n or and an \  ,so we eliminated them , so that we could name the csv file for each release by its tag
    with open(r"C:\Users\User\Desktop\jsontests\test"+str(i)+".json") as input_file:
        
        lines = input_file.readlines()
        
        for n, j in enumerate(lines):
            if (j=='\\n'):
                
                lines[n]=''
        
        
        
        
    with open(r"C:\Users\User\Desktop\jsontests\test"+str(i)+".json", 'r') as  input_file  :
    
    

        json_decode=json.load(input_file,strict=False)
        
    
    
        if ("/" in tag2) :
        
            tag2=tag2.replace('/','')
        #now we should give the path of where the result will be stored
		
        with open(r"C:\Users\User\Desktop\Rminer_Results"+"\\"+result+"\\"+tag2+".csv",'w') as newFile:
            #from the output of rminer we extract only the id of commit , the type of refactoring , and the description of it
            newFileWriter = csv.writer(newFile)
            newFileWriter.writerow(['id','type of refactoring','description'])
            if(json_decode["commits"]==''):
                print("empty")
            else :
                
                    

      
                for item in json_decode["commits"]:
        
               
    
                    for refact in item.get('refactorings'):
                
                
                
            
                    
            
                        newFileWriter.writerow([item.get('sha1'),refact.get('type'),refact.get('description')])
        


print("The exit code was done")