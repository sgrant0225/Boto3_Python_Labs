import boto3

s3 = boto3.client('s3')

response = s3.generate_presigned_url('get_object', Params={'Bucket' : "cf-templates-1rjg3s4vy91tr-us-east-1", 'Key': "2023-05-18T004928.612Z0nd-1CreateS3BucketCF.yml"}, ExpiresIn=300)

print(response)