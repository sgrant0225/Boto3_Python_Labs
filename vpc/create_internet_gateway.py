import boto3

ec2 = boto3.client('ec2')

internet_gateway = ec2.create_internet_gateway()

print(internet_gateway["InternetGateway"])
