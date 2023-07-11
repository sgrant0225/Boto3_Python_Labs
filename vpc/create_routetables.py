import boto3

vpc_id = 'vpc-05049a764d0ed3acd'

ec2 = boto3.client('ec2')

route_table = ec2.create_route_table(VpcId=vpc_id)

print(route_table['RouteTable']['RouteTableId'])

