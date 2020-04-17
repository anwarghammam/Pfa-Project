# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 12:35:36 2020

@author: User
"""
import time
import subprocess
import csv, json, sys
import os
from os import walk
#give the name of the project to run
project=str(sys.argv[1])
#give the git url of the project
url = str(sys.argv[2])
#give the path of the rfolder where the result will be stored
target=str(sys.argv[3])
tags=[]
#the tags of releases willbe stored in file designite.json
file = open(r"C:\Users\User\Desktop\designite.json", 'w')

list_files = subprocess.run(["git","tag"] ,stdout=file,shell=True)

with open(r"C:\Users\User\Desktop\designite.json") as file:
    
    for line in file: 
        line=str(line.rstrip("\n"))
        
        
        tags.append(line)
# locate in the folder where the releases will be cloned
os.chdir(r"C:\Users\User\Desktop\designite"+"\\"+project)

for tag in tags :

 
    list_files = subprocess.run(["git","clone",url,tag],shell=True)

#give the path of folder where the releases were cloned
mypath=r"C:\Users\User\Desktop\designite"+"\\"+project

#change the current postion to the folder where DesgniteJava jar is stored

os.chdir(r"C:\Users\User\Desktop")
f = []
for i in range(len(tags)):
    #this will generate for each releases 4  csv files  containing informations about the code smells , implementation smells and other metrics
    list_files=subprocess.run(["java" ,"-jar","DesigniteJava.jar","-i",mypath+"\\"+tags[i], "-o" ,target],shell=True)
    

