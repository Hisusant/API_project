import pymongo
# mongodb application server
client = pymongo.MongoClient("mongodb+srv://susant:susant123@cluster0.8beoc.mongodb.net/?retryWrites=true&w=majority")
db = client.test
#print(db)
# creating database
database = client['db22']

data = {
    "name" : "sushanta",
    "mail_id" : "skpsushanta@gmail.com",
    "subject" : ["data scinece" , "big data " , "data analytics "]
}

# table creation
collection = database['employ2']


# inset data to MongoDB cloud
collection.insert_one(data)

list_of_records = [

    {
        'companyName' : 'TechnoApp software solutions',
        'product' : 'Medical program',
        'courses' : 'AI'
    },
    {
        'companyName' : 'ineuron',
        'product' : 'bachelor program',
        'courses' : 'DS'
    },
    {
        'companyName': 'ineuron',
        'product': 'master degree',
        'courses': 'Python'
    }

]
# insert datta to server
collection.insert_many(list_of_records)
