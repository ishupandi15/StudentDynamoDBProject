# uploadToS3.py
import boto3
import json
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentRecords')
s3 = boto3.client('s3')
BUCKET_NAME = 'your-name-student-records-bucket'  # replace with your real bucket

def export_to_s3():
    response = table.scan()
    students = response.get('Items', [])

    tmp_path = "/tmp/students_export.json"
    with open(tmp_path, "w") as f:
        json.dump(students, f, default=str)

    s3.upload_file(tmp_path, BUCKET_NAME, "students_export.json")
    print("Data exported to S3 bucket:", BUCKET_NAME)

if __name__ == "__main__":
    export_to_s3()
