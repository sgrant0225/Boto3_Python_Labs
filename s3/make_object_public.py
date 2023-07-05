import boto3 

s3 = boto3.client('s3')

bucket = 'cf-templates-1rjg3s4vy91tr-us-east-1'
key = 'blue_image.jpg'

response = s3.put_public_access_block(
    Bucket=bucket,
   
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,
        'IgnorePublicAcls': False,
        'BlockPublicPolicy': False,
        'RestrictPublicBuckets': False
    }
)

response = s3.put_bucket_ownership_controls(
    Bucket=bucket,
    OwnershipControls={
        'Rules': [
            {
                'ObjectOwnership': 'BucketOwnerPreferred'
            },
        ]
    }
)

response = s3.put_bucket_acl(
    ACL='private',
    Bucket=bucket,
   )

response = s3.put_object_acl(ACL='public-read', Bucket=bucket, Key=key)

print(response)

#In this code we made the bucket public 
