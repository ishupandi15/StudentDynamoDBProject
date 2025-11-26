# deleteStudent.py
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentRecords')

def delete_student(student_id):
    response = table.delete_item(Key={'student_id': int(student_id)})
    print("Deleted response metadata:", response.get('ResponseMetadata'))

if __name__ == "__main__":
    # Example: delete student id 4
    delete_student(4)
