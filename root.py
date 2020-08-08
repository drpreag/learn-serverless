import json


def root_get(event, context):
    message = "Hi, this is / endpoint!"

    body = {
        "message": message,
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def hello_get(event, context):
    message = "Hi, this is /hello endpoint!"

    if event["pathParameters"] is not None:
        if event["pathParameters"]["name"] is not None:
            message = message + " Parameter is " + event["pathParameters"]["name"] + " !"

    body = {
        "message": message
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