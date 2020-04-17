#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:36:05 2020
@author: ichraf
"""

import pandas as pd
import subprocess
from find_bug_fix_vbugzilla import find_bug_fixes
from find_bug_fixes_vgithub import find_bug_fixe_github
import json ,sys


"""we have to clone all release that we will work with because some release repeated the same (same commit)
but with different tag """
def clone_all_releases(tags_commits, repo_url ) :
 
    file=open(tags_commits)
    lines=file.readlines()
    lines=lines[1:]
    tags=[]
    commits=[]
 
    for index, line in enumerate(lines) :
        
        tag=line.split(',')[0].split("refs/tags/")[1].replace(" ","")
        commit=line.split(',')[1]
  
        if commit not in commits :
            tags.append(tag)
            commits.append(commit)  

            if index ==0  :
              
               process=subprocess.Popen("git clone "+repo_url+" --branch  "+tag+" "+tag ,shell=True)
               process.wait()
               
            elif  index >0 :
                previous_tag=lines[index-1].split(",")[0].split("refs/tags/")[1]
                process=subprocess.Popen("git clone "+repo_url+" --branch  "+tag+" --shallow-exclude="+previous_tag+" "+tag ,shell=True)
                process.wait()
                
    return tags , commits 

import os
def run_szz_per_release(path_tags_commits,repo_url,issue_path,project_local,pattern) :
     
    tags,commits=clone_all_releases(path_tags_commits,repo_url)
    """ the releases are in the chronological order we inversed to start with the most recent one
    because the fix commit is in it's last appareance 
    """ 
    print("all_issues")
    tags=tags[::-1]
    commits=commits[::-1]
        
    releases_file=[]
    for index ,tag in enumerate(tags) :
       
        # run the file that create gitlog.json
        proc=subprocess.Popen("python3  git_log_to_array.py  --repo-path "+tag+" --from-commit "+commits[index],  shell=True)
        proc.wait()
        print("git fetch end")
            
        # get the current directory and the previous command will create gitlog file
        directory=os.getcwd()
        gitlog_path=os.path.join(directory, 'gitlog.json')
        #pattern="[Bb][Zz]-\d+"
        #find issue fixed in release 
        if ".csv" in issue_path:
            issue_list=find_bug_fixes(issue_path,gitlog_path,pattern)
        else :
            issue_list=find_bug_fixe_github(issue_path,gitlog_path,pattern)
            
        print(len(issue_list))
        # if the list of issues not empty => remove from issues from list of total issues
        if issue_list !={} :
                
                
            remove_issue(issue_list,issue_path)
            
            releases_file.append(tag)
            # list of issues
            with open('issue_list_'+tag+'.json', 'w') as f :
            
                f.write(json.dumps(issue_list))
                f.close()
    
    
    for tag in releases_file :
        subprocess.call("java -jar szz_find_bug_introducers-0.1.jar -i issue_list_"+tag+".json  -r "+project_local+" ; zip -r "+tag+".zip issues results  ; rm -rf issues results" ,shell=True)
        
                

def remove_issue(issue_list,issue_path):
    if ".csv" in issue_path :
        remove_issues_csv(issue_list,issue_path)
    else : 
        remove_issues_github(issue_list,issue_path)

def remove_issues_csv(issue_list,issue_path):
    
    data =pd.read_csv(issue_path)
    
    for issue in issue_list :
       
        if (data['Bug ID'] ==issue).any() :
            issue_to_remove=data[data['Bug ID']==issue]
            data.drop(issue_to_remove.index,axis=0,inplace=True)
            
    data.to_csv(issue_path,index=False,sep=",")        

def remove_issues_github(issue_list,issue_path):
    with open(issue_path) as f:
        all_issues=json.load(f)
        for index ,issue in enumerate(all_issues):
            if issue['number'] in issue_list :
                all_issues.pop(index)

    with open(issue_path, 'w') as data_file:
        json.dump(all_issues, data_file)        
            

    
    
tags_commits_path=str(sys.argv[1])
pattern=str(sys.argv[2])
git_repo_url=str(sys.argv[3])
issue_path=str(sys.argv[4])
project_local=str(sys.argv[5])


run_szz_per_release(tags_commits_path,git_repo_url,issue_path,project_local,pattern)        
