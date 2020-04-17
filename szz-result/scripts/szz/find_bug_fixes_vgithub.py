#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:49:28 2020

@author: ichraf
"""


import os
import json
import re
import argparse , sys

def find_bug_fixe_github(issue_path, gitlog_path, gitlog_pattern):
    """ Identify bugfixes in repository given a list of issues """

    no_matches = []
    matches_per_issue = {}
    total_matches = 0

    issue_list = build_issue_list(issue_path)
 
    with open(gitlog_path) as f:
        gitlog = json.loads(f.read())
    
    # for each issue in list search for it's fix in gitlog file
    for key in issue_list:
       
      
        key_str=str(key)
        matches = []
        pattern = gitlog_pattern.replace("\d+",key_str)
        
        for commit in gitlog:
                
            #pattern="#"+key_str+"\s|#"+key_str+"[)]"
            #pattern="[Ii]ssue "+key_str+" |# "+key_str+" |#"+key_str+" |#"+key_str+"[)]"
                
            if re.search(pattern, commit):           
                matches.append(commit)
        
        total_matches += len(matches)
        
        matches_per_issue[key] = len(matches)

        if matches:
            # get the commit which actually fix the issue  
            selected_commit = commit_selector_heuristic(matches)
            # add the sha of the fix commit and the it's date to the issue
            if selected_commit :
                issue_list[key]['hash'] = \
                re.search('(?<=^commit )[a-z0-9]+(?=\n)', \
                          selected_commit).group(0)
                issue_list[key]['commitdate'] = \
                re.search('(?<=\nDate:   )[0-9 -:+]+(?=\n)',\
                        selected_commit).group(0)
        
        # if the issue wasn't found add it the no_matches list         
        else:
            no_matches.append(key)


    print('Total issues: ' + str(len(issue_list)))
    print('Issues matched to a bugfix: ' + str(len(issue_list) - len(no_matches)))
    print('Percent of issues matched to a bugfix: ' + \
          str((len(issue_list) - len(no_matches)) / len(issue_list)))
    
    # remove issues without fix from list
    for key in no_matches:
        issue_list.pop(key)
    
    return issue_list


def build_issue_list(file_path):
    """ Helper method for find_bug_fixes """
    issue_list = {}
    
    #for each issue set it's creation date and resolution date
    with open(file_path) as f:
        for issue in json.loads(f.read()):
            issue_list[issue['number']] = {}
            
            created_date = issue['created_at'].replace('T', ' ')
            created_date = created_date.replace('Z', ' ')
            created_date = created_date.replace('.000', ' ')
            created_date= created_date+"+0000"
           
            issue_list[issue['number']]['creationdate'] = created_date

            res_date = issue['closed_at'].replace('T', ' ')
            res_date = res_date.replace('Z', ' ')
            res_date = res_date.replace('.000', ' ')
            res_date=res_date+"+0000"
            issue_list[issue['number']]['resolutiondate'] = res_date
    
    return issue_list

def commit_selector_heuristic(commits):
    """ Helper method for find_bug_fixes.
    Commits are assumed to be ordered in reverse chronological order.
    Given said order, pick first commit that does not match the pattern.
    If all commits match, return newest one. """
    for commit in commits:

        if not re.search('[Mm]erge|[Cc]herry|[Nn]oting', commit):
            return commit
    return commits[0]


"""if you want to test this script uncomment next lines 
(we used this script in the szz.py to get issue list per release that's why we comment this part)"""

#issue_path=str(sys.argv[1])
#gitlog_path=str(sys.argv[2])
#pattern=str(sys.argv[3])
#issues=find_bug_fixes(issue_path,gitlog_path,pattern)
#with open('issue_list.json', 'w') as f:   
#    f.write(json.dumps(issues))

