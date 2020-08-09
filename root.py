import json

def root(event, context):
    message = "Hi, this is / endpoint!"

    body = {
        "message": message,
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def hello(event, context):
    message = "Hi, this is /hello endpoint!"

    body = {
        "message": message,
        #"input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def hello_name(event, context):
    message = "Hi, this is /hello/name endpoint!"

    if "pathParameters" in event:
        if "id" in event["pathParameters"]:
            message = "Hi, this is /hello/name/id/" + event["pathParameters"]["id"] + " endpoint !"

    body = {
        "message": message,
        #"input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def hello_post(event, context):
    message = "Hi, this is /hello POST endpoint!"
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