import boto3



ec2 = boto3.client('ec2')

associate_routetable = ec2.associate_route_table(
    RouteTableId='rtb-0648a4cbf77358758',
    SubnetId='subnet-0fbed17e961d8375b',
)

print(associate_routetable['AssociationId'])