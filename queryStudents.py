# queryStudents.py
import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentRecords')

def query_students():
    # Scan for grade A
    response = table.scan(
        FilterExpression=Attr('grade').eq('A')
    )
    print("Students with grade A:")
    for student in response.get('Items', []):
        print(student)

    # Full scan for gender counts (small dataset is ok)
    response = table.scan()
    items = response.get('Items', [])
    males = sum(1 for s in items if s.get('gender') == 'Male')
    females = sum(1 for s in items if s.get('gender') == 'Female')

    print("Total Male Students:", males)
    print("Total Female Students:", females)

if __name__ == "__main__":
    query_students()
