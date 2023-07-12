import boto3

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId='vpc-05049a764d0ed3acd',
)


