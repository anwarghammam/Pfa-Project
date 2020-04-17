# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 16:11:23 2020

@author: ASUS
"""
import subprocess
import sys
import csv
import pandas as pd
import numpy as np

from os import walk 
lines_filtred=[]
#input is the name of the  prooject
input = str(sys.argv[1])
#mypathl is the path ot he folder where ths csv files after cleaning will be stored 
mypath1=r"C:\Users\User\Desktop\nouveau dossier"
f1 = []
classes=0
data=pd.DataFrame([{'ClassName': "com.ibm.jit.JITHelpers"}])
for (dirpath, dirnames, filenames) in walk(mypath1):
    f1.extend(filenames)
    for i in f1 :
        
    
        with open(mypath1+"\\"+i, "r") as txtfile:
            for line in txtfile:
                line=line.rstrip("\n")
                if((str(line)!="Move Source Folder")and(str(line)!="Change Package")):
                    
                    data[line+" in"]=0 
                    data[line+" out"]=0 
print(data.columns)   
#mypath is the path of the folder where the data before cleaning is strored
mypath=r"C:\Users\User\Desktop\my career\PFA\pfa sheets\Rminer_Results"+"\\"+input
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    
    f.extend(filenames)
    print(filenames)
numberClass = 0
# at this part of code , we will start cleaning each release
# for each line from the csv file we will analyse the description of the refactoring and extract the class in and the class out 
# each type of refactoring  has its own code to extract the class out( source class of the reefactoring )and the class in (target class of the refactoring)   ,
#in total we have 39 type of refactoring the code above will analyse each refactoring type
for i in f :
    
    print(i)
    
    with open(mypath+"\\"+i, "r") as csv_file:
    
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        
        for lines in csv_reader:
            
            
			
            if  (lines['type of refactoring']=="Extract Variable") :
                
               
                
                position = lines['description'].rfind('from class')
                Class=str(lines['description'])[position+11:]
                print(str(lines['description'])[position+11:])

                if (Class  not in data.values):
                    
                   
    
                    print(Class)
                    data.loc[data.shape[0]+1] = [Class] +[0]*78
                    
                if((data[data['ClassName']==Class].index.values).size!=0):
                
                
                    index=data[data['ClassName']==Class].index.values.astype(int)[0]
                    
                
                    data.at[index,"Extract Variable out"]=data.at[index,"Extract Variable out"]+1
                    

 
            if  (lines['type of refactoring']=="Merge Parameter") :
                
               
                
                position = lines['description'].rfind('in class')
                Class=str(lines['description'])[position+9:]
                
    
                print(Class)

                if (Class  not in data.values):
                    
                    
                    data.loc[data.shape[0]+1] = [Class] +[0]*78
               
                if((data[data['ClassName']==Class].index.values).size!=0):
                
                
                    index=data[data['ClassName']==Class].index.values.astype(int)[0]
                        
                    print(index)
                    data.at[index,"Merge Parameter out"]=data.at[index,"Merge Parameter out"]+1
                    print(data.at[index,"Merge Parameter out"])


              
            if  (lines['type of refactoring']=="Rename Parameter") :
                
               
                
                position = lines['description'].rfind('in class')
                Class=str(lines['description'])[position+9:]
                Class.replace(' ','')
                Class.replace('\n','')
                Class.replace('"','')

                if (Class  not in data.values):
                    
                    
                    data.loc[data.shape[0]+1] = [Class] +[0]*78
               
                if((data[data['ClassName']==Class].index.values).size!=0):
                
                
                    index=data[data['ClassName']==Class].index.values.astype(int)[0]
                    
                    print(index)
                    data.at[index,"Rename Parameter out"]=data.at[index,"Rename Parameter out"]+1
                    print(data.at[index,"Rename Parameter out"])

            if  (lines['type of refactoring']=="Change Variable Type") :
                
                
               
                
                position = lines['description'].rfind('in class')
                Class=str(lines['description'])[position+9:]
                Class.replace(' ','')
                Class.replace('\n','')
                Class.replace('"','')

                if (Class  not in data.values):
                    
                    print(Class)
                    data.loc[data.shape[0]+1] = [Class] +[0]*78
               
                if((data[data['ClassName']==Class].index.values).size!=0):
                
                
                    index=data[data['ClassName']==Class].index.values.astype(int)[0]
                    print(index)   
                    
                    data.at[index,"Change Variable Type out"]=data.at[index,"Change Variable Type out"]+1
                    print(data.at[index,"Change Variable Type out"])

            if  (lines['type of refactoring']=="Rename Variable") :
                
                
               
                
                position = lines['description'].rfind('in class')
                Class=str(lines['description'])[position+9:]
               

                if (Class  not in data.values):
                    
                    
                    data.loc[data.shape[0]+1] = [Class] +[0]*78
               
                if((data[data['ClassName']==Class].index.values).size!=0):
                
                
                    index=data[data['ClassName']==Class].index.values.astype(int)[0]
                        
                    print(data[data['ClassName']==Class].index.values.astype(int))
                    data.at[index,"Rename Variable out"]=data.at[index,"Rename Variable out"]+1
                    print(data.at[index,"Rename Variable out"])
            
            
            
            
            if  (lines['type of refactoring']=="Rename Method") :
                
               
                position = lines['description'].rfind('in class')
                Class=str(lines['description'])[position+9:]
                
                
                if (Class  not in data.values):
                    
                    print(Class)
                    data.loc[data.shape[0]+1] = [Class] +[0]*78
               
                if((data[data['ClassName']==Class].index.values).size!=0):
                
                
                    index=data[data['ClassName']==Class].index.values.astype(int)[0]
                    print(index)   
                    
                    data.at[index,"Rename Method out"]=data.at[index,"Rename Method out"]+1
                    print(data.at[index,"Rename Method out"])
            



            
            
            
            if  (lines['type of refactoring']=="Change Attribute Type") :
                
               
                position = lines['description'].rfind('in class')
                Class=str(lines['description'])[position+9:]
                

                if (Class  not in data.values):
                    
                    
                    data.loc[data.shape[0]+1] = [Class] +[0]*78
                    print(Class)
                if((data[data['ClassName']==Class].index.values).size!=0):
                
                
                    index=data[data['ClassName']==Class].index.values.astype(int)[0]
                    print(index)   
                    
                    data.at[index,"Change Attribute Type out"]=data.at[index,"Change Attribute Type out"]+1
                    print(data.at[index,"Change Attribute Type out"])

            
            
            if  (lines['type of refactoring']=="Rename Attribute") :
                
               
                position = lines['description'].rfind('in class')
                Class=str(lines['description'])[position+9:]
                

                if (Class  not in data.values):
                    
                    
                    data.loc[data.shape[0]+1] = [Class] +[0]*78
                    print(Class)
                if((data[data['ClassName']==Class].index.values).size!=0):
                
                
                    index=data[data['ClassName']==Class].index.values.astype(int)[0]
                        
                    print(index)
                    data.at[index,"Rename Attribute out"]=data.at[index,"Rename Attribute out"]+1
                    print(data.at[index,"Rename Attribute out"])
            
            
            if  (lines['type of refactoring']=="Merge Variable") :
                
               
                position = lines['description'].rfind('in class')
                Class=str(lines['description'])[position+9:]
                

                if (Class  not in data.values):
                    
                    
                    data.loc[data.shape[0]+1] = [Class] +[0]*78
                    print(Class)
                if((data[data['ClassName']==Class].index.values).size!=0):
                
                
                    index=data[data['ClassName']==Class].index.values.astype(int)[0]
                    print(index)    
                    
                    data.at[index,"Merge Variable out"]=data.at[index,"Merge Variable out"]+1
                    print(data.at[index,"Merge Variable out"])



            if  (lines['type of refactoring']=="Parameterize Variable") :
                
               
                position = lines['description'].rfind('in class')
                Class=str(lines['description'])[position+9:]
                
                if (Class  not in data.values):
                    
                    
                    data.loc[data.shape[0]+1] = [Class] +[0]*78
                    print(Class)
                if((data[data['ClassName']==Class].index.values).size!=0):
                
                
                    index=data[data['ClassName']==Class].index.values.astype(int)[0]
                    print(index)
                    data.at[index,"Parameterize Variable out"]=data.at[index,"Parameterize Variable out"]+1
                    
                    
                    
                    print(data.at[index,"Parameterize Variable out"])

            
            
            if  (lines['type of refactoring']=="Split Attribute") :
                
               
                position = lines['description'].rfind('in class')
                Class=str(lines['description'])[position+9:]
                
                if (Class  not in data.values):
                    
                    
                    data.loc[data.shape[0]+1] = [Class] +[0]*78
                    print(Class)
                if((data[data['ClassName']==Class].index.values).size!=0):
                
                
                    index=data[data['ClassName']==Class].index.values.astype(int)[0]
                    data.at[index,"Split Attribute out"]=data.at[index,"Split Attribute out"]+1
                    print(index)
                    
                    print(data.at[index,"Split Attribute out"])

            if  (lines['type of refactoring']=="Split Parameter") :
                
               
                position = lines['description'].rfind('in class')
                Class=str(lines['description'])[position+9:]
               
                if (Class  not in data.values):
                    
                    
                    data.loc[data.shape[0]+1] = [Class] +[0]*78
               
                if((data[data['ClassName']==Class].index.values).size!=0):
                
                
                    index=data[data['ClassName']==Class].index.values.astype(int)[0]
                    data.at[index,"Split Parameter out"]=data.at[index,"Split Parameter out"]+1
                   

            if  (lines['type of refactoring']=="Split Variable") :
                
               
                position = lines['description'].rfind('in class')
                Class=str(lines['description'])[position+9:]
                

                if (Class  not in data.values):
                    
                    
                    data.loc[data.shape[0]+1] = [Class] +[0]*78
                    print(Class)
                if((data[data['ClassName']==Class].index.values).size!=0):
                
                
                    index=data[data['ClassName']==Class].index.values.astype(int)[0]
                    data.at[index,"Split Variable out"]=data.at[index,"Split Variable out"]+1
                    print(index)
                    
                    print(data.at[index,"Split Variable out"])



            if  (lines['type of refactoring']=="Merge Attribute") :
                
               
                
                position = lines['description'].rfind('in class')
                Class=str(lines['description'])[position+9:]
                

                if (Class  not in data.values):
                    
                    
                    data.loc[data.shape[0]+1] = [Class] +[0]*78
                    print(Class)
                if((data[data['ClassName']==Class].index.values).size!=0):
                
                
                    index=data[data['ClassName']==Class].index.values.astype(int)[0]
                        
                    print(index)
                    data.at[index,"Merge Attribute out"]=data.at[index,"Merge Attribute out"]+1
                    print(data.at[index,"Merge Attribute out"])           




            
            if  (lines['type of refactoring']=="Move Method") :
                
               
                
                position_out = lines['description'].find('from class')
                position_in = lines['description'].rfind('from class')
                sep = lines['description'].find('to ')
                Class_in=str(lines['description'])[position_out+11:sep -1]
                Class_out=str(lines['description'])[position_in+11:]
                


                if (Class_in not in data.values):
                    data.loc[data.shape[0]] = [Class_in] +[0]*78
                    
                if (Class_out not in data.values):
                    data.loc[data.shape[0]] = [Class_out] +[0]*78
                    

                        

                if((data[data['ClassName']==Class_in].index.values).size!=0):
                    
                
                
                    index_in=data[data['ClassName']==Class_in].index.values.astype(int)[0]
                    print(index_in)
                   
                    data.at[index_in,"Move Method in"]=data.at[index_in,"Move Method in"]+1
                
                if((data[data['ClassName']==Class_out].index.values).size!=0):
                    
                
                
                    index_out=data[data['ClassName']==Class_out].index.values.astype(int)[0]
                    print(index_out)
                
                    data.at[index_out,"Move Method out"]=data.at[index_out,"Move Method out"]+1           
            
            
        


            if  (lines['type of refactoring']=="Change Parameter Type") :
                
                
               
                
                position = lines['description'].rfind('in class')
                Class=str(lines['description'])[position+9:]
                

                if (Class  not in data.values):
                    
                    print(Class)
                    data.loc[data.shape[0]+1] = [Class] +[0]*78
               
                if((data[data['ClassName']==Class].index.values).size!=0):
                
                
                    index=data[data['ClassName']==Class].index.values.astype(int)[0]
                    print(index)   
                    
                    data.at[index,"Change Parameter Type out"]=data.at[index,"Change Parameter Type out"]+1
                    print(data.at[index,"Change Parameter Type out"])


            if  (lines['type of refactoring']=="Change Return Type") :
                
                
               
                
                position = lines['description'].rfind('in class')
                Class=str(lines['description'])[position+9:]
                

                if (Class  not in data.values):
                    
                    print(Class)
                    data.loc[data.shape[0]+1] = [Class] +[0]*78
               
                if((data[data['ClassName']==Class].index.values).size!=0):
                
                
                    index=data[data['ClassName']==Class].index.values.astype(int)[0]
                    print(index)   
                    
                    data.at[index,"Change Return Type out"]=data.at[index,"Change Return Type out"]+1
                    print(data.at[index,"Change Return Type out"])





            
            
            
            
            
            
            if  (lines['type of refactoring']=="Move Class") :
                
               
                
                position_out = lines['description'].find('Move Class')
                position_in = lines['description'].rfind('to')
                sep = lines['description'].find('moved to ')
                Class_out=str(lines['description'])[position_out+11:sep-1]
                Class_in=str(lines['description'])[position_in+3:]
                print(Class_in)
                print(Class_out)
#

                if (Class_in not in data.values):
                    data.loc[data.shape[0]] = [Class_in] +[0]*78
                    
                if (Class_out not in data.values):
                    data.loc[data.shape[0]] = [Class_out] +[0]*78
                    

                        
#                print(data[data['ClassName']==Class_in].index.values.astype(int)[0])
#                print(data[data['ClassName']==Class_out].index.values.astype(int)[0])
                if((data[data['ClassName']==Class_in].index.values).size!=0):
                    
                
                
                    index_in=data[data['ClassName']==Class_in].index.values.astype(int)[0]
                    print(index_in)
                   
                    data.at[index_in,"Move Class in"]=data.at[index_in,"Move Class in"]+1
                
                if((data[data['ClassName']==Class_out].index.values).size!=0):
                    
                
                
                    index_out=data[data['ClassName']==Class_out].index.values.astype(int)[0]
                    print(index_out)
                
                    data.at[index_out,"Move Class out"]=data.at[index_out,"Move Class out"]+1







            if  (lines['type of refactoring']=="Move And Rename Attribute") :
                
               
                
                position_out = lines['description'].rfind('from class')
                position_in = lines['description'].rfind('to class')
                
                Class_out=str(lines['description'])[position_out+11:position_out-1]
                Class_in=str(lines['description'])[position_out+9:]
                print(Class_in)
                print(Class_out)
#

                if (Class_in not in data.values):
                    data.loc[data.shape[0]] = [Class_in] +[0]*78
                    
                if (Class_out not in data.values):
                    data.loc[data.shape[0]] = [Class_out] +[0]*78
                    

                        
#                print(data[data['ClassName']==Class_in].index.values.astype(int)[0])
#                print(data[data['ClassName']==Class_out].index.values.astype(int)[0])
                if((data[data['ClassName']==Class_in].index.values).size!=0):
                    
                
                
                    index_in=data[data['ClassName']==Class_in].index.values.astype(int)[0]
                    print(index_in)
                   
                    data.at[index_in,"Move And Rename Attribute in"]=data.at[index_in,"Move And Rename Attribute in"]+1
                
                if((data[data['ClassName']==Class_out].index.values).size!=0):
                    
                
                
                    index_out=data[data['ClassName']==Class_out].index.values.astype(int)[0]
                    print(index_out)
                
                    data.at[index_out,"Move And Rename Attribute out"]=data.at[index_out,"Move And Rename Attribute out"]+1




    

            
            
            
            
            
            if  (lines['type of refactoring']=="Pull Up Method") :
                
               
                
                position_out = lines['description'].find('from class')
                position_in = lines['description'].rfind('from class')
                sep = lines['description'].find('to')
                Class_out=str(lines['description'])[position_out+11:sep-1]
                Class_in=str(lines['description'])[position_in+11:]
                print(Class_out)
                print(Class_in)
#

                if (Class_in not in data.values):
                    data.loc[data.shape[0]] = [Class_in] +[0]*78
                    
                if (Class_out not in data.values):
                    data.loc[data.shape[0]] = [Class_out] +[0]*78
                    

                        
#                print(data[data['ClassName']==Class_in].index.values.astype(int)[0])
#                print(data[data['ClassName']==Class_out].index.values.astype(int)[0])
                if((data[data['ClassName']==Class_in].index.values).size!=0):
                    
                
                
                    index_in=data[data['ClassName']==Class_in].index.values.astype(int)[0]
                    print(index_in)
                   
                    data.at[index_in,"Pull Up Method in"]=data.at[index_in,"Pull Up Method in"]+1
                
                if((data[data['ClassName']==Class_out].index.values).size!=0):
                    
                
                
                    index_out=data[data['ClassName']==Class_out].index.values.astype(int)[0]
                    print(index_out)
                
                    data.at[index_out,"Pull Up Method out"]=data.at[index_out,"Pull Up Method out"]+1
            

            
            
            if  (lines['type of refactoring']=="Pull Up Attribute") :
                
               
                
                position_out = lines['description'].find('from class')
                position_in = lines['description'].rfind('from class')
                sep = lines['description'].find('to')
                Class_out=str(lines['description'])[position_out+11: sep -1]
                Class_in=str(lines['description'])[position_in+11:]
               
#

                if (Class_in not in data.values):
                    data.loc[data.shape[0]] = [Class_in] +[0]*78
                    
                if (Class_out not in data.values):
                    data.loc[data.shape[0]] = [Class_out] +[0]*78
                    

                        
#                print(data[data['ClassName']==Class_in].index.values.astype(int)[0])
#                print(data[data['ClassName']==Class_out].index.values.astype(int)[0])
                if((data[data['ClassName']==Class_in].index.values).size!=0):
                    
                
                
                    index_in=data[data['ClassName']==Class_in].index.values.astype(int)[0]
                    print(index_in)
                   
                    data.at[index_in,"Pull Up Attribute in"]=data.at[index_in,"Pull Up Attribute in"]+1
                
                if((data[data['ClassName']==Class_out].index.values).size!=0):
                    
                
                
                    index_out=data[data['ClassName']==Class_out].index.values.astype(int)[0]
                    print(index_out)
                
                    data.at[index_out,"Pull Up Attribute out"]=data.at[index_out,"Pull Up Attribute out"]+1            
            
            
            
            if  (lines['type of refactoring']=="Push Down Method") :
                
               
                
                position_out = lines['description'].find('from class')
                position_in = lines['description'].rfind('from class')
                sep = lines['description'].find('to')
                Class_out=str(lines['description'])[position_out+11:sep-1]
                Class_in=str(lines['description'])[position_in+11:]
                print(Class_out)
                print(Class_in)
#

                if (Class_in not in data.values):
                    data.loc[data.shape[0]] = [Class_in] +[0]*78
                    
                if (Class_out not in data.values):
                    data.loc[data.shape[0]] = [Class_out] +[0]*78
                    

                        
#                print(data[data['ClassName']==Class_in].index.values.astype(int)[0])
#                print(data[data['ClassName']==Class_out].index.values.astype(int)[0])
                if((data[data['ClassName']==Class_in].index.values).size!=0):
                    
                
                
                    index_in=data[data['ClassName']==Class_in].index.values.astype(int)[0]
                    print(index_in)
                   
                    data.at[index_in,"Push Down Method in"]=data.at[index_in,"Push Down Method in"]+1
                
                if((data[data['ClassName']==Class_out].index.values).size!=0):
                    
                
                
                    index_out=data[data['ClassName']==Class_out].index.values.astype(int)[0]
                    print(index_out)
                
                    data.at[index_out,"Push Down Method out"]=data.at[index_out,"Push Down Method out"]+1            
            
            
            if  (lines['type of refactoring']=="Push Down Attribute") :
                
               
                
                position_out = lines['description'].find('from class')
                position_in = lines['description'].rfind('from class')
                sep = lines['description'].find('to')
                Class_out=str(lines['description'])[position_out+11:sep-1]
                Class_in=str(lines['description'])[position_in+11:]
                print(Class_out)
                print(Class_in)
#

                if (Class_in not in data.values):
                    data.loc[data.shape[0]] = [Class_in] +[0]*78
                    
                if (Class_out not in data.values):
                    data.loc[data.shape[0]] = [Class_out] +[0]*78
                    

                        
#                print(data[data['ClassName']==Class_in].index.values.astype(int)[0])
#                print(data[data['ClassName']==Class_out].index.values.astype(int)[0])
                if((data[data['ClassName']==Class_in].index.values).size!=0):
                    
                
                
                    index_in=data[data['ClassName']==Class_in].index.values.astype(int)[0]
                    print(index_in)
                   
                    data.at[index_in,"Push Down Attribute in"]=data.at[index_in,"Push Down Attribute in"]+1
                
                if((data[data['ClassName']==Class_out].index.values).size!=0):
                    
                
                
                    index_out=data[data['ClassName']==Class_out].index.values.astype(int)[0]
                    print(index_out)
                
                    data.at[index_out,"Push Down Attribute out"]=data.at[index_out,"Push Down Attribute out"]+1            
                        



            if  (lines['type of refactoring']=="Rename Class") :
                
               
                
                position_out = lines['description'].find('Rename Class')
                position_in = lines['description'].rfind('renamed to')
                sep = lines['description'].find('renamed to')
                Class_out=str(lines['description'])[position_out+13:sep-1]
                Class_in=str(lines['description'])[position_in+11:]
                print(Class_out)
                print(Class_in)
#

                if (Class_in not in data.values):
                    data.loc[data.shape[0]] = [Class_in] +[0]*78
                    
                if (Class_out not in data.values):
                    data.loc[data.shape[0]] = [Class_out] +[0]*78
                    

                        
#                print(data[data['ClassName']==Class_in].index.values.astype(int)[0])
#                print(data[data['ClassName']==Class_out].index.values.astype(int)[0])
                if((data[data['ClassName']==Class_in].index.values).size!=0):
                    
                
                
                    index_in=data[data['ClassName']==Class_in].index.values.astype(int)[0]
                    print(index_in)
                   
                    data.at[index_in,"Rename Class in"]=data.at[index_in,"Rename Class in"]+1
                
                if((data[data['ClassName']==Class_out].index.values).size!=0):
                    
                
                
                    index_out=data[data['ClassName']==Class_out].index.values.astype(int)[0]
                    print(index_out)
                
                    data.at[index_out,"Rename Class out"]=data.at[index_out,"Rename Class out"]+1   
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
            if  (lines['type of refactoring']=="Rename Method") :
                
               
                position = lines['description'].rfind('in class')
                Class=str(lines['description'])[position+9:]
                

                print(Class)

                if (Class not in data.values):
                    
                    numberClass = numberClass +1
                    data.loc[data.shape[0]+1] = [Class] +[0]*78
               
                if((data[data['ClassName']==Class].index.values).size!=0):
                
                
                    index=data[data['ClassName']==Class].index.values.astype(int)[0]
                    print(index)
                    data.at[index,"Rename Method in"]=data.at[index,"Rename Method in"]+1
#                    print(data[data['ClassName']==Class].index.values.astype(int))
                    
                    print(data.at[index,"Rename Method in"])
            
            
            if  (lines['type of refactoring']=="Move Method") :
                
               
                
                position_in = lines['description'].find('from class')
                position_out = lines['description'].rfind('from class')
                sep = lines['description'].find('to ')
                Class_in=str(lines['description'])[position_in+11:sep-1]
                Class_out=str(lines['description'])[position_out+11:]
                print(Class_in)
                print(Class_out)
#

                if (Class_in not in data.values):
                    data.loc[data.shape[0]] = [Class_in] +[0]*78
                    numberClass =numberClass +1
                if (Class_out not in data.values):
                    data.loc[data.shape[0]] = [Class_out] +[0]*78
                    numberClass =numberClass +1

                        
#                print(data[data['ClassName']==Class_in].index.values.astype(int)[0])
#                print(data[data['ClassName']==Class_out].index.values.astype(int)[0])
                if((data[data['ClassName']==Class_in].index.values).size!=0):
                    
                
                
                    index_in=data[data['ClassName']==Class_in].index.values.astype(int)[0]
                    print(index_in)
                   
                    data.at[index_in,"Move Method in"]=data.at[index_in,"Move Method in"]+1
                
                if((data[data['ClassName']==Class_out].index.values).size!=0):
                    
                
                
                    index_out=data[data['ClassName']==Class_out].index.values.astype(int)[0]
                    print(index_out)
                
                    data.at[index_out,"Move Method out"]=data.at[index_out,"Move Method out"]+1

     
    
    
    
    
    
    
    
    
    
    
    
    
    
            if  (lines['type of refactoring']=="Extract Method") or  (lines['type of refactoring']=="Extract Atrribute"):
             
                    
                 position = lines['description'].rfind('in class')
                 Class=str(lines['description'])[position+9:]
                 
                        
    
                        
                 if (Class not in data.values) :
                     
                            
                        
                     data.loc[data.shape[0]+1] = [Class] +[0]*78
                     
                   
                 if((data[data['ClassName']==Class].index.values).size!=0):
                     
                     
                    
                    
                    
                     index=data[data['ClassName']==Class].index.values.astype(int)[0]
                        
                    
                    
                     if  (lines['type of refactoring']=="Extract Method"):
                         
                         
                            
                         data.at[index,"Extract Method in"]=data.at[index,"Extract Method in"]+1
                         print(data.at[index,"Extract Method in"])
                     else :
                            
                            
                         data.at[index,"Extract Attribute in"]=data.at[index,"Extract Attribute in"]+1
                         print(data.at[index,"Extract Attribute in"])
                         
    
    
    
    
                     
            if  (lines['type of refactoring']=="Inline Method") :
                        
                
                    
                   
                    
                position = lines['description'].rfind('in class')
                Class=str(lines['description'])[position+9:]
                
                print(str(lines['description'])[position+9:])
    
                if (Class not in data.values):
                    
                
                    data.loc[data.shape[0]+1] = [Class] +[0]*78
                   
                if((data[data['ClassName']==Class].index.values).size!=0):
                    
                    
                    index=data[data['ClassName']==Class].index.values.astype(int)[0]
                        
                    
                    data.at[index,"Inline Method in"]=data.at[index,"Inline Method in"]+1
#                
            if  (lines['type of refactoring']=="Inline Variable") :
                
                
               
                
                position = lines['description'].rfind('from class')
                Class=str(lines['description'])[position+11:]
               
                
                print(str(lines['description'])[position+11:])
    
                if (Class not in data.values):
                        
                        
                    data.loc[data.shape[0]+1] = [Class] +[0]*78
                   
                if((data[data['ClassName']==Class].index.values).size!=0):
                    
                    
                    index=data[data['ClassName']==Class].index.values.astype(int)[0]
                        
                
                    data.at[index,"Inline Variable in"]=data.at[index,"Inline Variable in"]+1
                
            if  (lines['type of refactoring']=="Move And Inline Method") :
                    
                   
                    
                position_out = lines['description'].rfind('from class')
                position_in = lines['description'].rfind('to class')
                sep = lines['description'].rfind('&')
                Class_out=str(lines['description'])[position_out+11:position_in-1]
                Class_in=str(lines['description'])[position_in+9:sep-1]
                
                if (Class_out not in data.values):
                        
                    data.loc[data.shape[0]] = [Class_out] +[0]*78
                
                        
                if (Class_in not in data.values):
                    data.loc[data.shape[0]+1] = [Class_in] +[0]*78
                
                if((data[data['ClassName']==Class_out].index.values).size!=0):
                        
                    
                    
                        index_out=data[data['ClassName']==Class_out].index.values.astype(int)[0]
                        
                       
                        data.at[index_out,"Move And Inline Method out"]=data.at[index_out,"Move And Inline Method out"]+1
                    
                if((data[data['ClassName']==Class_in].index.values).size!=0):
                        
                    
                    
                        index_in=data[data['ClassName']==Class_in].index.values.astype(int)[0]
                        
                    
                        data.at[index_in,"Move And Inline Method in"]=data.at[index_in,"Move And Inline Method in"]+1
            
            if  (lines['type of refactoring']=="Replace Attribute") :
                    
                position_out = lines['description'].find('from class')
                    
                    
                position_in = lines['description'].rfind('from class')
                sep = lines['description'].rfind('with ')
                Class_in=str(lines['description'])[position_out+11:sep-1]
                Class_out=str(lines['description'])[position_in+11:]
                
                    
                    
    
                if (Class_out in data.values):
                    
                    data.loc[data.shape[0]] = [Class_out] +[0]*78
                    
                        
                if (Class_in not in data.values):
                    data.loc[data.shape[0]+1] = [Class_in] +[0]*78
                    
                if((data[data['ClassName']==Class_out].index.values).size!=0):
                        
                    
                    
                    index_out=data[data['ClassName']==Class_out].index.values.astype(int)[0]
                        
                       
                    data.at[index_out,"Replace Attribute out"]=data.at[index_out,"Replace Attribute out"]+1
                    
                if((data[data['ClassName']==Class_in].index.values).size!=0):
                        
                    
                    
                    index_in=data[data['ClassName']==Class_in].index.values.astype(int)[0]
                        
                    
                    data.at[index_in,"Replace Attribute in"]=data.at[index_in,"Replace Attribute in"]+1
# 
    
            if  (lines['type of refactoring']=="Replace Variable With Attribute") :
                
                position = lines['description'].rfind('in class')
                
                Class=str(lines['description'])[position+9:]
                
                    
                if (Class not in data.values):
                    
                        
                        
                    data.loc[data.shape[0]+1] = [Class] +[0]*78
                    
                   
                if((data[data['ClassName']==Class].index.values).size!=0):
                    
                    
                    index=data[data['ClassName']==Class].index.values.astype(int)[0]
                    
                    data.at[index,"Replace Variable With Attribute in"]=data.at[index,"Replace Variable With Attribute in"]+1
            
            if  (lines['type of refactoring']=="Extract And Move Method") :
                
                
                
               
                
                position_out = lines['description'].rfind('in class')
                position_in = lines['description'].rfind('to class')
                sep = lines['description'].rfind('&')
                Class_out=str(lines['description'])[position_out+9:sep-1]
                Class_in=str(lines['description'])[position_in+9:]
                

                if (Class_out not in data.values):
                    
                    data.loc[data.shape[0]] = [Class_out] +[0]*78
            
                    
                if (Class_in not in data.values):
                    data.loc[data.shape[0]+1] = [Class_in] +[0]*78
                print(Class_in)        
                print(data[data['ClassName']==Class_in].index.values.astype(int)[0])
                print(Class_out)   
                print(data[data['ClassName']==Class_out].index.values.astype(int)[0])
                if((data[data['ClassName']==Class_out].index.values).size!=0):
                
                    
                
                
                    index_out=data[data['ClassName']==Class_out].index.values.astype(int)[0]
                    
                   
                    data.at[index_out,"Extract And Move Method out"]=data.at[index_out,"Extract And Move Method out"]+1
                
                if((data[data['ClassName']==Class_in].index.values).size!=0):
                    
                
                
                    index_in=data[data['ClassName']==Class_in].index.values.astype(int)[0]
                    
                
                    data.at[index_in,"Extract And Move Method in"]=data.at[index_in,"Extract And Move Method in"]+1
                    
                    
                    
            if  (lines['type of refactoring']=="Extract Class") :
             
                
                
               
                
                 position_in = lines['description'].rfind('Extract Class')
                 position_out = lines['description'].rfind('from class')
                 
                 Class_out=str(lines['description'])[position_out+11:]
                 Class_in=str(lines['description'])[position_in+14:position_out-1]
                    
    
                 if (Class_out not in data.values):
                     
                    
                        
                     data.loc[data.shape[0]] = [Class_out] +[0]*78
                
                        
                 if (Class_in not in data.values):
                    
                     data.loc[data.shape[0]+1] = [Class_in] +[0]*78
                 
                 if((data[data['ClassName']==Class_out].index.values).size!=0):
                    
                        
                    
                    
                     index_out=data[data['ClassName']==Class_out].index.values.astype(int)[0]
                        
                       
                     data.at[index_out,"Extract Class out"]=data.at[index_out,"Extract Class out"]+1
                    
                 if((data[data['ClassName']==Class_in].index.values).size!=0):
                     
                        
                    
                    
                     index_in=data[data['ClassName']==Class_in].index.values.astype(int)[0]
                        
                    
                     data.at[index_in,"Extract Class in"]=data.at[index_in,"Extract Class in"]+1
                     
                     
            
            if  (lines['type of refactoring']=="Move Attribute") :
                position_out = lines['description'].find('from class')
                position_in = lines['description'].rfind('from class')
                sep = lines['description'].rfind('to ')
                Class_out=str(lines['description'])[position_out+11:sep-1]
                Class_in=str(lines['description'])[position_in+11:]
                

                if (Class_out not in data.values):
                    data.loc[data.shape[0]] = [Class_out] +[0]*78
            
                    
                if (Class_in not in data.values):
                    data.loc[data.shape[0]+1] = [Class_in] +[0]*78
                
                if((data[data['ClassName']==Class_out].index.values).size!=0):
                    index_out=data[data['ClassName']==Class_out].index.values.astype(int)[0]
                    
                   
                    data.at[index_out,"Move Attribute out"]=data.at[index_out,"Move Attribute out"]+1
                
                if((data[data['ClassName']==Class_in].index.values).size!=0):
                    
                
                
                    index_in=data[data['ClassName']==Class_in].index.values.astype(int)[0]
                    
                
                    data.at[index_in,"Move Attribute in"]=data.at[index_in,"Move Attribute in"]+1   
            
            if  (lines['type of refactoring']=="Move And Rename Method") :
                position_out = lines['description'].find('from class')
                position_in = lines['description'].rfind('from class')
                sep = lines['description'].find('to ')
                Class_out=str(lines['description'])[position_out+11:sep-1]
                Class_in=str(lines['description'])[position_in+11:]
                

                if (Class_out not in data.values):
                    data.loc[data.shape[0]] = [Class_out] +[0]*78
            
                    
                if (Class_in not in data.values):
                    data.loc[data.shape[0]+1] = [Class_in] +[0]*78
                print(Class_in)        
                print(data[data['ClassName']==Class_in].index.values.astype(int)[0])
                print(Class_out)   
                print(data[data['ClassName']==Class_out].index.values.astype(int)[0])
                if((data[data['ClassName']==Class_out].index.values).size!=0):
                    index_out=data[data['ClassName']==Class_out].index.values.astype(int)[0]
                    
                   
                    data.at[index_out,"Move And Rename Method out"]=data.at[index_out,"Move And Rename Method out"]+1
                
                if((data[data['ClassName']==Class_in].index.values).size!=0):
                    
                
                
                    index_in=data[data['ClassName']==Class_in].index.values.astype(int)[0]
                    
                
                    data.at[index_in,"Move And Rename Method in"]=data.at[index_in,"Move And Rename Method in"]+1   
#                    
#                    
            if  (lines['type of refactoring']=="Move And Rename Class") :
                
                position_out = lines['description'].find('Rename Class')
                position_in = lines['description'].rfind('renamed to')
                sep = lines['description'].find('moved ')
                Class_out=str(lines['description'])[position_out+13:sep-1]
                Class_in=str(lines['description'])[position_in+11:]
                

                if (Class_out not in data.values):
                    data.loc[data.shape[0]] = [Class_out] +[0]*78
            
                    
                if (Class_in not in data.values):
                    data.loc[data.shape[0]+1] = [Class_in] +[0]*78
                
                if((data[data['ClassName']==Class_out].index.values).size!=0):
                    index_out=data[data['ClassName']==Class_out].index.values.astype(int)[0]
                    
                   
                    data.at[index_out,"Move And Rename Class out"]=data.at[index_out,"Move And Rename Class out"]+1
                
                if((data[data['ClassName']==Class_in].index.values).size!=0):
                    
                
                
                    index_in=data[data['ClassName']==Class_in].index.values.astype(int)[0]
                    
                
                    data.at[index_in,"Move And Rename Class in"]=data.at[index_in,"Move And Rename Class in"]+1   
            
                                
        
                    
                    
            
            if  (lines['type of refactoring']=="Extract Subclass") :
                    position_in = lines['description'].find('Extract Subclass')
                    position_out = lines['description'].rfind('from class')
                
                    Class_in=str(lines['description'])[position_in+17:position_out-1]
                    Class_out=str(lines['description'])[position_out+11:]
                

                    if (Class_out not in data.values):
                        data.loc[data.shape[0]] = [Class_out] +[0]*78
            
                    
                    if (Class_in not in data.values):
                        data.loc[data.shape[0]+1] = [Class_in] +[0]*78
                        print(Class_in)        
                        print(data[data['ClassName']==Class_in].index.values.astype(int)[0])
                        print(Class_out)   
                        print(data[data['ClassName']==Class_out].index.values.astype(int)[0])
                        if((data[data['ClassName']==Class_out].index.values).size!=0):
                            index_out=data[data['ClassName']==Class_out].index.values.astype(int)[0]
                    
                   
                        data.at[index_out,"Extract Subclass out"]=data.at[index_out,"Extract Subclass out"]+1
                
                    if((data[data['ClassName']==Class_in].index.values).size!=0):
                    
                
                
                        index_in=data[data['ClassName']==Class_in].index.values.astype(int)[0]
                    
                
                
                        data.at[index_in,"Extract Subclass in"]=data.at[index_in,"Extract Subclass in"]+1
            
            if  (lines['type of refactoring']=="Extract Interface") :
                     
                     position= lines['description'].find('from classes [')
                     liste=lines['description'][position+14:]
                     
                     while (liste !=""):
                         
                         premier_virgule=liste.find(',')
                         if (premier_virgule==-1):
                            
                             
                         
                             Class_out=liste[:liste.find(']')]
                             print(Class_out)
                             if (Class_out not in data.values):
                                
                             
                                 data.loc[data.shape[0]] = [Class_out] +[0]*78
                             if((data[data['ClassName']==Class_out].index.values).size!=0):
                                 index_out=data[data['ClassName']==Class_out].index.values.astype(int)[0]
                    
                   
                             data.at[index_out,"Extract Superclass out"]=data.at[index_out,"Extract Superclass out"]+1
                             liste=""
                         
                         else :
                             
                            
                             Class_out=liste[:premier_virgule]
                             print(Class_out)
                             if (Class_out not in data.values):
                             
                                 data.loc[data.shape[0]] = [Class_out] +[0]*78
                             if((data[data['ClassName']==Class_out].index.values).size!=0):
                                 
                                 index_out=data[data['ClassName']==Class_out].index.values.astype(int)[0]
                                 data.at[index_out,"Extract Superclass out"]=data.at[index_out,"Extract Superclass out"]+1    
                             liste=liste[premier_virgule+2:]
    
                      
                
                
            if  (lines['type of refactoring']=="Extract Superclass") :
                
                
                    
                    
                position_in=lines['description'].find('Extract Superclass')
                    
                     
                     
                position= lines['description'].find('from classes [')
                Class_in=str(lines['description'])[position_in+19:position-1]
                print(Class_in)
                if (Class_in not in data.values):
                    
                        
                
                    data.loc[data.shape[0]+1] = [Class_in] +[0]*78
            
                if((data[data['ClassName']==Class_in].index.values).size!=0):
                    
                    
                         
                
                    index_in=data[data['ClassName']==Class_in].index.values.astype(int)[0]
                    
                   
                    data.at[index_in,"Extract Superclass in"]=data.at[index_in,"Extract Superclass in"]+1
                liste=lines['description'][position+14:]
                while (liste !=""):
                    
                   
                    premier_virgule=liste.find(',')
                    if (premier_virgule==-1):
                            
                             
                         
                        Class_out=liste[:liste.find(']')]
                        print(Class_out)
                        if (Class_out not in data.values):
                                
                             
                            data.loc[data.shape[0]] = [Class_out] +[0]*78
                        if((data[data['ClassName']==Class_out].index.values).size!=0):
                            index_out=data[data['ClassName']==Class_out].index.values.astype(int)[0]
                    
                   
                        data.at[index_out,"Extract Superclass out"]=data.at[index_out,"Extract Superclass out"]+1
                        liste=""
                         
                    else :
                            
                        Class_out=liste[:premier_virgule]
                        print(Class_out)
                        if (Class_out not in data.values):
                             
                            data.loc[data.shape[0]] = [Class_out] +[0]*78
                        if((data[data['ClassName']==Class_out].index.values).size!=0):
                            index_out=data[data['ClassName']==Class_out].index.values.astype(int)[0]
                            data.at[index_out,"Extract Superclass out"]=data.at[index_out,"Extract Superclass out"]+1    
                        liste=liste[premier_virgule+2:]
#    
    print(data) 
    data1=data.loc[1:,:]      
    data1.to_csv(r'C:\Users\User\Desktop\resultat'+'\\'+input+'\\'+str(i),index=False)
    data.iloc[0:0]
    