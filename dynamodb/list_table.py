import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.get_item(
    TableName='mymoviereleases',
    Key={
        'movieid': {
            'S': '1',
        },
    },
)

print(response['Item'])



# response = dynamodb.describe_table(
#     TableName='mymoviereleases',
# )

# print(response)
