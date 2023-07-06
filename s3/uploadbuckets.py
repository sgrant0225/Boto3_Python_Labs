import boto3
#import os

s3 = boto3.client('s3')

# with open("test_text.txt", 'rb') as f:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
#     s3.put_object(Bucket="cf-templates-1rjg3s4vy91tr-us-east-1", Key="test_text.txt", Body=f, ContentType="text/plain")
    
# with open("/Boto3_Python_Labs/S3/test_text.txt", 'rb') as data:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
#     s3.upload_fileobj(data, "cf-templates-1rjg3s4vy91tr-us-east-1", "test_text.txt", ExtraArgs={'ContentType':'text/plain'})

s3.upload_file('test_text.txt', 'cf-templates-1rjg3s4vy91tr-us-east-1', 'test_text.txt', ExtraArgs={'ContentType':'text/plain'})

print 
