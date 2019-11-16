from pymongo import MongoClient
import dns

client = MongoClient("mongodb+srv://test:test@cluster0-eqh5v.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('users')
users = db.users

test_user = {
    'user' : 'alex',
    'password' : 'gandon',
    'id' : ['1','2']
    }

result = users.insert(test_user)
print("Data inserted!")

