import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.scan(
    ExpressionAttributeNames={
        '#FG': 'FoodGroup',
        '#FN': 'Name',
    },
    ExpressionAttributeValues={
        ':f': {
            'S': 'Protein',
        },
    },
    FilterExpression='FoodGroup = :f',
    ProjectionExpression='#FG, #FN',
    TableName='myfavoritefoods',
)

print(response)
