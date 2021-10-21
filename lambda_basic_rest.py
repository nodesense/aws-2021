import json
import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # TODO implement
    logger.info('## ENVIRONMENT VARIABLES')
    logger.info(os.environ)
    logger.info('## EVENT')
    logger.info(event)
    
    body = event["body"]
    data = json.loads(body)
    logger.info("Product name is " + data["name"])
    
    return {
        'statusCode': 200,
        'body': json.dumps({"result": "success"}),
        "headers": { "X-ENCRYPTED": "true", "content-type": "application/json"},

    }
