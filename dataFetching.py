import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["assignment3"]

mycol1 = mydb["twitterData"]
mycol2 = mydb["newsData"]

data1 = ''
data2 = ''
for x in mycol1.find():
    data1 = data1  +" "+ (x['tweetText'].lower())

for y in mycol2.find():
    data2 = data2 +" "+ (y['content'].lower())

data = data1 + data2

f= open("data.txt","w+")
f.write(data)
f.close()

