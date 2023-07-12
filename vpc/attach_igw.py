import boto3 

ec2 = boto3.client('ec2')

ec2.attach_internet_gateway(
    InternetGatewayId='igw-0635f3b548b6c05a9',
    VpcId='vpc-05049a764d0ed3acd',
)

