import boto3 

dynamodb = boto3.client('dynamodb')

#create table
response = dynamodb.create_table(
    
#define the table name and schema 
TableName = 'myfavoritefoods',
#An array of attributes that describe the key schema for the table and indexes.
AttributeDefinitions=[
    {
        'AttributeName': 'ID',
        'AttributeType': 'S',
    },
    {
        'AttributeName': 'Name',
        'AttributeType': 'S'
    },
    
],
#This specifies the attributes that make up the primary key for a table or an index
KeySchema=[
    {
        'AttributeName': 'ID',
        'KeyType': 'HASH',
    },
    {
        'AttributeName': 'Name',
        'KeyType': 'RANGE',
    }
],
# Define the provisioned throughput
ProvisionedThroughput={
    'ReadCapacityUnits': 1,
    'WriteCapacityUnits': 1,
  }

)

print(response)