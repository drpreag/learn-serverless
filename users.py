import json
import pymongo
import sys

def users(event, context):
    message = "Hi, this is /users endpoint!"

    client = pymongo.MongoClient('mongodb://admin:servo123@test.cluster-cfzdxpdb0knm.eu-west-1.docdb.amazonaws.com:27017/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred')
    db = client.sample_database
    users = db.users

    body = {
        "message": message,
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def user(event, context):
    message = "Hi, this is /user/id/{id} endpoint!"

    if "pathParameters" in event:
        if "id" in event["pathParameters"]:
            message = "Hi, this is /user/id/{" + event["pathParameters"]["id"] + "} endpoint !"


    body = {
        "message": message,
        #"input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def user(event, context):
    message = "Hi, this is /user/email/{email} endpoint!"

    if "pathParameters" in event:
        if "email" in event["pathParameters"]:
            message = "Hi, this is /user/email/{" + event["pathParameters"]["email"] + "} endpoint !"


    body = {
        "message": message,
        #"input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def user_add_post(event, context):
    message = "Hi, this is /user/add POST endpoint!"
    request = []

    for key, value in json.loads (event["body"]).items():
        request.append ([key,value])

    body = {
        "message": message,
        "request": request
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
