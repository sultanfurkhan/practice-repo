import json
import boto3
def lambda_handler(event, context):
  client = boto3.client('ec2')
  responce = client.run_instances(
    ImageId='ami-0f71013b2c8bd2c29',
    InstanceType='t2.small',
    KeyName='mykey',
    MaxCount=1,
    MinCount=1
)
