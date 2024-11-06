import json
import boto3
def lambda_handler(event, context):

  client = boto3.client('s3')
  responce = client.run_isnstances(
    ImageId='ami-0f71013b2c8bd2c29',
    InstanceType='t2.micro3',
    KeyName='awskey',
    MaxCount=1,
    MinCount=1
)
