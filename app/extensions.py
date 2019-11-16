"""Extensions module - Set up for additional libraries can go in here."""
from pymongo import MongoClient

client = MongoClient("mongodb://admin:<admin>@cluster0-shard-00-00-eqh5v.mongodb.net:27017,cluster0-shard-00-01-eqh5v.mongodb.net:27017,cluster0-shard-00-02-eqh5v.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")

db = client.admin
