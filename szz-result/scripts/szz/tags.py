#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 23:35:38 2020

@author: ichraf
"""

import subprocess
import numpy as np 
import pandas as pd 
from dateutil.parser import parse

def getLastCommitPerTag():
    
    # get all the tags of the project and save it in file
    file=open("tag.txt","w")
    process = subprocess.Popen("git for-each-ref --sort=creatordate --format '%(refname) , %(creatordate)' refs/tags", 
                           stdout=file,
                           shell=True)
    #write until the process finish 
    process.wait()
    
    #get all the tags found 
    file=open("tag.txt","r")
    tags_dates=file.readlines()
    dates=[]
    tags=[]
    
    
    for tag_date in tags_dates :
        
        
	#    tag_date_splited=tag_date.split(",")
        
        tags.append(tag_date.split(",")[0])
        dates.append(parse(tag_date.split(",")[1].replace('\n','')).strftime('%Y-%m-%d %H:%M:%S %z'))
        
	
    print(dates)
    tag_commit=open("tag.txt","w")
    
    # for every tag get the corespondant commit
    for tag in tags :
        proc = subprocess.Popen("git rev-list -n 1 "+tag , stdout=tag_commit,shell=True)
        proc.wait()



    # get all commits and tags
    commits_file=open("tag.txt","r")
    
    all_commits=np.array(commits_file.readlines())
    all_commits=[commit.replace("\n","") for commit in all_commits]
    
    all_tags=np.array(tags)
    all_dates=np.array(dates)
    #combine tag to it commit and then write in csv
    df = pd.DataFrame({"tag" : all_tags, "commit" : all_commits , "creationdate":all_dates})
    
    df.to_csv("tags_commits.csv",index=False)        
    
getLastCommitPerTag()    
    
