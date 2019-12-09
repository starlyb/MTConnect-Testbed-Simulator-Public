import pymongo

#////////////////////////////////////////////////""
file = open("parameters.txt","r+")
parameters=dict()
lines = file.readlines()
for i in lines:
    temp=i.split("=")
    parameters[temp[0]]=temp[1]
file.close()
Dburl ="mongodb://localhost:"+str(parameters["MongoPort"])
######################################

myclient = pymongo.MongoClient(Dburl)

mydb = myclient["mtconnectdatabase"]
mycol = mydb["orders"]

myquery = { "PartID":'F' }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)