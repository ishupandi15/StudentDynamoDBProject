# updateStudent.py
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentRecords')

def update_student(student_id, new_grade):
    response = table.update_item(
        Key={'student_id': int(student_id)},
        UpdateExpression="SET grade = :g",
        ExpressionAttributeValues={':g': new_grade},
        ReturnValues="UPDATED_NEW"
    )
    print("Updated:", response.get('Attributes'))

if __name__ == "__main__":
    # Example usage: update student id 2 to grade A
    update_student(2, "A")
