import boto3 

ec2 = boto3.client('ec2')

subnet = ec2.create_subnet(CidrBlock='12.0.5.0/24', VpcId='vpc-05049a764d0ed3acd')
    
print(subnet['Subnet']['SubnetId'])
