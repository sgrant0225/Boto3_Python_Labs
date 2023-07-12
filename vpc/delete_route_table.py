import boto3 

ec2 = boto3.client('ec2')

ec2.delete_route_table(
    RouteTableId='rtb-0648a4cbf77358758'
)


