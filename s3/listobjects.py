import boto3

s3 = boto3.client('s3')

response = s3.list_objects_v2(Bucket="cf-templates-1rjg3s4vy91tr-us-east-1")

for content in response['Contents']:
    print(content['Key'])