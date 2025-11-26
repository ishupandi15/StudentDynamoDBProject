# insertFromFile.py
import boto3
import json
import os
import sys
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentRecords')

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

def get_json_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    candidate = os.path.join(script_dir, 'students.json')
    if os.path.exists(candidate):
        return candidate
    fallback = '/mnt/data/students-1-1.json'
    if os.path.exists(fallback):
        return fallback
    return None

def insert_data():
    path = get_json_path()
    if not path:
        print("ERROR: students.json not found. Put students.json next to this script or /mnt/data/students-1-1.json")
        sys.exit(1)

    print(f"Loading student data from: {path}")
    with open(path, 'r') as f:
        students = json.load(f)
        for student in students:
            # Ensure student_id is numeric for DynamoDB numeric key
            if 'student_id' in student:
                student['student_id'] = int(student['student_id'])
            table.put_item(Item=student)
    print("Data inserted successfully.")

if __name__ == "__main__":
    insert_data()
