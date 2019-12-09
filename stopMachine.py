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

myquery = { "_id": "20Mach1" }
#myquery = { "PartID": "GZ" }
newvalues = { "$set": { "Order": 789789}}

mycol.update_one(myquery, newvalues)

#myquery = { "_id": "24Mach4"}
#
#mydoc = mycol.find(myquery)
#
#for x in mydoc:
#  print(x)