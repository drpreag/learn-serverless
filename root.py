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
            message = "Hi, this is /hello endpoint! Parameter is " + event["pathParameters"]["name"] + " !"

    body = {
        "message": message,
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def hello_post(event, context):
<<<<<<< HEAD
    message = "Hi, this is /hello POST endpoint!"

    if event["pathParameters"] is not None:
        if event["pathParameters"]["name"] is not None:
            message = "Hello man " + event["pathParameters"]["name"] + " !"
=======
    message = "/hello post request"
    request = []
    dict = json.loads(event["body"])

    for key, value in dict.items():
        request.append ([key, value])
>>>>>>> 6ae23fd96e85454197a1d121e9fc0edf8a7562dc

    body = {
        "message": message,
        "request": request
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response