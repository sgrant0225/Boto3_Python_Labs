import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.get_item(
    TableName='mymoviereleases',
    Key={
        'movieid': {
            'S': '1',
        },
        'genre': {
            'S': 'Fantasy',
        },
        'title': {
            'S': 'The Little Mermaid',
        },
        'rating': {
            'S': 'G',
        },
    },
)

print(response['Key'])

# response = dynamodb.describe_table(
#     TableName='mymoviereleases',
# )

# print(response)
