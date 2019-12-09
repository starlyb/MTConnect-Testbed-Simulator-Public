
import os
import pandas as pd
import shutil
import time
import subprocess
import send2trash as s2t

################################
file = open("parameters.txt","r+")
parameters=dict()
lines = file.readlines()
for i in lines:
    temp=i.split("=")
    parameters[temp[0]]=temp[1]
file.close()
Dburl ="mongodb://localhost:"+str(parameters["MongoPort"])
try:
    os.popen("net start MongoDB")
except:
    pass
##################################

master = pd.read_csv('dbs\master.csv')
orgs = list(master['names'])
DIR=(os.getcwd())


def father():
    subprocess.call(['python', 'father.py'])
 
def master():
    subprocess.call(['python', 'master_init.py'])

def moadp():
    subprocess.call(['python', 'mother_adp.py'])

def moagent():
    os.chdir(DIR)
    os.system("python mother_agents.py")
def momap():
    os.chdir(DIR)
    os.system("python mother_map.py")
def moxml():
    os.chdir(DIR)
    os.system("python mother_xmls.py")
def index():
    p=subprocess.Popen(['python', 'index.py'])
    print(p.pid)
    
    
def init():
    os.chdir(DIR)
    os.startfile("init.bat")
    os.chdir(DIR)
    
def startAgent():
    master = pd.read_csv('dbs\master.csv')
    orgs = list(master['names'])
    for i in range(len(orgs)):
        path=DIR+'/temp_folder/Org '+str(i+1)+'/'
        os.chdir(path)
        os.startfile("startAgent.bat")
        os.chdir(DIR)
    
def startAdps():
    master = pd.read_csv('dbs\master.csv')
    orgs = list(master['names'])
    for i in range(len(orgs)):
        path=DIR+'/temp_folder/Org '+str(i+1)+'/'
        os.chdir(path)
        os.startfile("batchStart.bat")
        os.chdir(DIR)

def stopAgent():
    import pymongo
   
    myclient = pymongo.MongoClient(Dburl)
    mydb = myclient["mtconnectdatabase"]
    mycol = mydb["orders"]
    mycol.drop()
    master = pd.read_csv('dbs\master.csv')
    orgs = list(master['names'])
    for i in range(len(orgs)):
        path=DIR+'/temp_folder/Org '+str(i+1)+'/'
        os.chdir(path)
        os.startfile("stopAgent.bat")
        os.chdir(DIR)
        
def stopAdps():
     for i in range(len(orgs)):
        path=DIR+'/temp_folder/Org '+str(i+1)+'/'
        os.chdir(path)
        os.startfile("batchKill.bat")
        os.chdir(DIR)


def reset():  
  dirpath=DIR+'\\temp_folder\\'         
  s2t.send2trash(dirpath)
  os.mkdir(DIR+'/temp_folder/')
    
def STOP():
    stopAgent()
    stopAdps()
    
def START():
    startAgent() 
    time.sleep(7)
    startAdps()
    
#reset()

#STOP()
#startAdps()
#reset()
#init()
#father()
#master()
#moadp()
#moagent()
#momap()
#moxml()
#startAgent()
#stopAdps()
#index()
#stopAgent()

