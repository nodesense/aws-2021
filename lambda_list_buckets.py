import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    s3 = boto3.resource('s3')
    
    buckets = []
    for bucket in s3.buckets.all():
        print(bucket.name)
        buckets.append(bucket.name)
        
    return {
        'statusCode': 200,
        'body': json.dumps(buckets)
    }
