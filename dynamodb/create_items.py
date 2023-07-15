import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.put_item(
    Item={
        'ID': {
            'S': '4',
        },
        'Name': {
            'S': 'Teriyaki Shrimp with vegetales',
        },
        'Origin': {
            'S': 'Japan',
        },
         'FoodGroup': {
            'S': 'Protein',
        },
    },
    ReturnConsumedCapacity='TOTAL',
    TableName='myfavoritefoods',
)

print(response)