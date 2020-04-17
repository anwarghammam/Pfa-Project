#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:02:49 2020

@author: ichraf ben fadhel
"""

import urllib.request as url
import json
import os , sys

def fetch_from_github(repo_owner , repo_name):
# we need token to get data from api 
    token="69b30b32f71f947bf7224abc4a884073d2f0fe3b"
#specifiy features in the request  
    request="https://api.github.com/repos/"+repo_owner+"/"+repo_name+"/issues?access_token="+token+"&state=closed&labels=bug&per_page=100&page="
    i=1 # number of page
    downloading=True 
    data=[]
    #create issues directory if it don't exist
    os.makedirs('issues', exist_ok=True)
    #continue downloading issues while there are data 
    while downloading :
       
        req = url.Request(request+str(i), headers={'User-Agent': 'Mozilla/5.0'})
        
        with url.urlopen(req) as conn:
            issues = json.loads(conn.read().decode('utf-8'))
            # when the result is empty mean we downloaded all issues => so stop  
            if issues ==[] :
                downloading =False
            else :
                # add  the downloaded data to issue list
                for issue in issues :
                    data.append(issue)
        # increment the page number to get  the next page            
        i+=1
    # write the issues in json file
    file_result_path=os.path.join('issues', repo_name+'.json') # to make it independent of the plateform 
    with open(file_result_path, 'w', encoding="utf-8") as f:
        f.write(json.dumps(data))
    print("file created => "+file_result_path)    

repo_owner= str(sys.argv[1])
repo_name=str(sys.argv[2])
fetch_from_github(repo_owner,repo_name)

#fetch_from_github("eclipse","openj9")
