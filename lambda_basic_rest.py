import json
import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # TODO implement
    print("My REST API")
    logger.info('## ENVIRONMENT VARIABLES')
    logger.info(os.environ)
    logger.info('## EVENT')
    logger.info(event)
    
    # POST method - it carries a payload as json content
    body = event["body"] # read data from api gateway
    data = json.loads(body) # parsing json string to json object
    logger.info("Product name is " + data["name"])
    
    return {
        'statusCode': 200,
        'body': json.dumps({"result": "success", "productName": data["name"]}),
        "headers": { "X-ENCRYPTED": "true", "content-type": "application/json"},

    }
