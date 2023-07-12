import boto3 

ec2 = boto3.client('ec2')

ec2.delete_internet_gateway(
    InternetGatewayId='igw-0635f3b548b6c05a9',
)

