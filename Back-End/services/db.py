from pymongo import MongoClient

Mongo_client = MongoClient("mongodb://capstone:mongopassword@cluster0-shard-00-00-we2hu.mongodb.net:27017,cluster0-shard-00-01-we2hu.mongodb.net:27017,cluster0-shard-00-02-we2hu.mongodb.net:27017/client_example?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
loggingdb = Mongo_client.logging.exceptions
# record = loggingdb.find_one({"log": ""})
# print(record)
