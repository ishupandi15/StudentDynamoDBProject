# createTable.py
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # set your region

def create_table():
    table = dynamodb.create_table(
        TableName='StudentRecords',
        KeySchema=[
            {'AttributeName': 'student_id', 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'student_id', 'AttributeType': 'N'}
        ],
        ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
    )
    table.wait_until_exists()
    print("Table created:", table.table_name)

if __name__ == "__main__":
    create_table()
