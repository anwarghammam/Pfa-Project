

import sys 
import pandas as pd

""" this script is used to rename jira features to be the same as bugzilla """
issue_path=str(sys.argv[1])

data=pd.read_csv(issue_path)

data.rename({"Issue key":"Bug ID","Created":"Opened"},axis='columns',inplace=True)

data.to_csv(issue_path,sep=",",index=False)
