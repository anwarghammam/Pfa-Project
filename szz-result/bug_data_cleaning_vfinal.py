#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:08:28 2020

@author: ichraf
"""
import subprocess 
import collections
import os ,sys
import pandas as pd 
def get_all_commit_fix(file_path,output_folder):
  
    file=open(file_path,"r")
   
    lines=file.read().splitlines()
    filtred_commits_intro_bug=[]
    bugs_tags=[]
    all_commits=[]
    for line in lines :
        line=line.replace('[',"").replace("]","")
        if line=="," :
            pass
        else :
            commits=line.split(",")
            all_commits.extend(commits[:len(commits)-1])
       
    fixes_commit,commits_intro_bug = all_commits[::2],all_commits[1::2]
    filtred_fixes_commit=[]
    

    
    # to eliminate redundency of the same commit bug from the same fix commit
    for index,commit_intro_bug in enumerate(commits_intro_bug):
        commit_intro_bug=commit_intro_bug.replace('"','')
        fixes_commit[index]=fixes_commit[index].replace('"','')
        check=verif_commit(commit_intro_bug,fixes_commit[index],filtred_commits_intro_bug,filtred_fixes_commit)
        if check ==-1 :
            filtred_commits_intro_bug.append(commit_intro_bug)
            filtred_fixes_commit.append(fixes_commit[index])
            
    
   # print(len(filtred_commits_intro_bug))
    
    # for every commit intro bug get which release it show 
    for bug_commit in filtred_commits_intro_bug :
        print(bug_commit)
        #tag_file=open('tag.txt',"w")
        #sort by tag creation date to get the first release 
        proc=subprocess.Popen(" git tag --contains="+bug_commit+"| xargs -I@ git log --format=format:'%ai @%n' -1 @ | sort | awk '{print $4}'", stdout=subprocess.PIPE,shell=True)        
        oldest_tag=proc.communicate()[0].decode('utf-8').split("\n")[0]
        bugs_tags.append(oldest_tag)
        
        
    print(bugs_tags)
    # for each release store it's commits introducing bug
    bugs_per_release={}
    bugs_per_release[bugs_tags[0]]=[]
    
    for index , tag in enumerate(bugs_tags) :
        if tag in bugs_per_release.keys():
            bugs_per_release[tag].append(filtred_commits_intro_bug[index])
        else :
            bugs_per_release[tag]=[]
            bugs_per_release[tag].append(filtred_commits_intro_bug[index])
    
            
    
    #for each commit bug , fix commit check the file modified => will represent the classes with bugs
    classes_modified_per_commit={}
    for index , commit_intro_bug in enumerate(filtred_commits_intro_bug) :
        if index >=0:
            print("commit intro")
            print(commit_intro_bug)
            modified_by_bug_commit=open("classes_bug_commit.txt","w")
            modified_by_fix_commit=open("classes_fix_commit.txt","w")

            print("commit fix")
            print(filtred_fixes_commit[0])
        #list of classes modified by bug commit  
            subprocess.call("git show -m --name-only --pretty=format: "+commit_intro_bug ,stdout=modified_by_bug_commit, shell=True)
            modified_by_bug_commit.close()
            
        # list of classes modified by fix commit 
            subprocess.call("git show -m --name-only --pretty=format: "+filtred_fixes_commit[index] ,stdout=modified_by_fix_commit, shell=True)
            modified_by_fix_commit.close()
            
            file=open("classes_affected.txt","w")
        #get the similarity between the two files 
            subprocess.call(" grep -f classes_bug_commit.txt classes_fix_commit.txt",stdout=file, shell=True)
            file.close()

        #get the result and add it to the dict
            file=open("classes_affected.txt","r")
            
            lines=file.read().splitlines()
            print("lines*****************")
            print(lines)
            classes=[]
            
            for line in lines :
                if line.endswith(".java") and 'org' in line :
                    line=line.replace(".java","").replace("/",".")
                    line=line[line.index("org"):]
                    classes.append(line)
                    
                    
            classes_modified_per_commit[commit_intro_bug]=classes
       
    print(classes_modified_per_commit)   
    # for each release we have it's list of bug commit and 
    for release , commit_bug_list in bugs_per_release.items() :
        all_classes_affected=[]
        # for each commit intro bug we get the classes affected by this commit       
        for commit in commit_bug_list :
        #    print(classes_modified_per_commit[commit])
            classes=classes_modified_per_commit[commit]
            if classes !=[] :
                all_classes_affected.extend(classes)
        if all_classes_affected !=[] :        
            # we get the list of classes affected in a release 
            count_per_class=dict(collections.Counter(all_classes_affected))
            keys=list(count_per_class.keys())
            values=list(count_per_class.values())
            df = pd.DataFrame({"ClassName" : keys, "nbBugs" : values })
            # write the result in csv file
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)     
            result_path=os.path.join(output_folder,release+".csv")
            df.to_csv(result_path,index=False)
      
        
def verif_commit(bug_commit , fix_commit, filtered_bug_commits,filtred_fix_commits) :
    for index, commit in enumerate(filtered_bug_commits) :
        if commit ==bug_commit and  filtred_fix_commits[index]==fix_commit :
            return 0
    return -1        
    
input_file=str(sys.argv[1])
output_folder=str(sys.argv[2])    
        
get_all_commit_fix(input_file,output_folder)        