from pymongo import MongoClient
import hashlib
import dns

def create_acc(user,pw):
    client = MongoClient("mongodb+srv://test:test@cluster0-eqh5v.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('users')
    users = db.users
    mysha1 = hashlib.sha1()
    pw = pw.encode('utf-8')
    mysha1.update(pw)
    hashedpw = mysha1.hexdigest()
    users.insert_one(
    {
    'user' : user,
    'password' : hashedpw ,
    'id' : []
    }
    )

def look_for(user):
    client = MongoClient("mongodb+srv://test:test@cluster0-eqh5v.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('users')
    users = db.users
    return (users.find_one({'user':user})) != None
def authenticate(user,pw):
    client = MongoClient("mongodb+srv://test:test@cluster0-eqh5v.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('users')
    pw = pw.encode('utf-8')
    mysha1 = hashlib.sha1()
    mysha1.update(pw)
    hashedpw = mysha1.hexdigest()
    users = db.users
    return (users.find_one({'user':user,'password':hashedpw})) != None
