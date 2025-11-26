# viewAllStudents.py
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentRecords')

def view_all():
    response = table.scan()
    for student in response.get('Items', []):
        print(student)

if __name__ == "__main__":
    view_all()
