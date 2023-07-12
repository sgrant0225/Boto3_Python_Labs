import boto3

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId='igw-0635f3b548b6c05a9',
    RouteTableId='rtb-0648a4cbf77358758',
)

