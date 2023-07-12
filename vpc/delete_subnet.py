import boto3

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId='subnet-0fbed17e961d8375b'
)


