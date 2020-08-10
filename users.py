import json
#import pymongo
import sys
import requests
from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib.parse

def users(event, context):
    client = MongoClient('mongodb+srv://sandbox_admin:GK6zEPpg3ADXx94@projectone.bjfes.mongodb.net/test?retryWrites=true&w=majority')
    users = client.test.users
    response = []

    query = users.find({}).limit(10)
    if users:
        for user in query:
            response.append ({ '_id': str(ObjectId(user['_id'])), 'name' : user['name'] , 'email': user['email'], 'password': user['password'] })
    else:
        return { "statusCode": 404 }

    response = {
        "statusCode": 200,
        "body": json.dumps({
            "users": response
        })
    }
    return response

def user_id(event, context):
    if "pathParameters" in event:
        if "id" in event["pathParameters"]:
            id = event["pathParameters"]["id"]

    if 'id' not in locals() or len(id)!=24:
        return { "statusCode": 404 }

    client = MongoClient('mongodb+srv://sandbox_admin:GK6zEPpg3ADXx94@projectone.bjfes.mongodb.net/test?retryWrites=true&w=majority')
    users = client.test.users
    user = users.find_one({ "_id": ObjectId(id) })
    if user:
        response = {
            "statusCode": 200,
            "body": json.dumps({
                "user": { '_id': str(ObjectId(user['_id'])), 'name' : user['name'] , 'email': user['email'], 'password': user['password'] }
            })
        }
    else:
        return { "statusCode": 404 }
    return response

def user_email(event, context):
    if "pathParameters" in event:
        if "email" in event["pathParameters"]:
            email = urllib.parse.unquote_plus(event["pathParameters"]["email"])

    if 'email' not in locals():
        return { "statusCode": 404 }

    client = MongoClient('mongodb+srv://sandbox_admin:GK6zEPpg3ADXx94@projectone.bjfes.mongodb.net/test?retryWrites=true&w=majority')
    users = client.test.users
    user = users.find_one({ "email":  email})
    if user:
        response = {
            "statusCode": 200,
            "body": json.dumps({
                "user": { '_id': str(ObjectId(user['_id'])), 'name' : user['name'] , 'email': user['email'], 'password': user['password'] }
            })
        }
    else:
        return { "statusCode": 404 }
    return response

def user_add_post(event, context):
    message = "Hi, this is /user/add POST endpoint!"
    request = []

    for key, value in json.loads (event["body"]).items():
        request.append ([key,value])

    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
            "request": request
        })
    }
    return response

def user_add(event, context):
    message = "Hi, this is /user/add GET endpoint!"
    client = MongoClient('mongodb+srv://sandbox_admin:GK6zEPpg3ADXx94@projectone.bjfes.mongodb.net/stest?retryWrites=true&w=majority')
    users = client.test.users

    user_id = users.insert_one ({"name": "Name one", "email":"Email one", "password": "blank" })

    body = {
        "message": message,
        "response": user_id
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response