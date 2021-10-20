import json

def lambda_handler(event, context):
    # TODO implement
    print("Hello world lambda")
    print("Here we add two numbers")
    print("event we got is ", json.dumps(event, indent=2))
    result = int(event["key1"]) + int(event["key2"]) + int(event["key3"])
    return {
        'statusCode': 200,
        'body': json.dumps('result is ' + str(result))
    }
