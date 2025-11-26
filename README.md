# Student Records CRUD Application using AWS DynamoDB & S3  
**Author:** Your Name  
**Project:** StudentRecords CRUD Application  
**Course:** AWS Learner Lab – Project 4  

---

## 📌 Project Overview  
This project implements a complete Student Records management system using AWS services.  
The system performs:

- Creation of a DynamoDB table  
- Uploading JSON student data  
- CRUD (Create, Read, Update, Delete) operations  
- Queries for grade “A” students and gender counts  
- Export of all DynamoDB data to S3 as a JSON file  

The project demonstrates the use of AWS Cloud9, DynamoDB, S3, and the boto3 SDK.

---

## 🛠 Technologies Used  
- **AWS Cloud9**  
- **AWS DynamoDB**  
- **AWS S3**  
- **Python 3**  
- **boto3 (AWS SDK)**  

---

## 📌 Part A: Create the DynamoDB Table  
The file `createTable.py` creates a DynamoDB table named **StudentRecords**.  
The table uses:

- `student_id` as the Partition Key  
- Data type: Number  

---

## 📌 Part B: Insert Student Data  
`insertFromFile.py` reads data from `students.json` and inserts each student record into the DynamoDB table.  
Each record contains:

- Student ID  
- Name  
- Gender  
- Grade  
- Transportation method  

---

## 📌 Part C: CRUD Operations  

### View All Students  
`viewAllStudents.py` retrieves and displays all records stored in the DynamoDB table.

### Update Student Grade  
`updateStudent.py` updates a student’s grade using their `student_id`.

### Delete a Student  
`deleteStudent.py` deletes a student record from DynamoDB using their `student_id`.

---

## 📌 Part D: Querying Student Data  
`queryStudents.py` performs two queries:

1. Lists all students who received grade **A**  
2. Counts how many male and female students are in the dataset  

---

## 📤 Export Data to S3  
The script `uploadToS3.py`:

- Reads all items from DynamoDB  
- Converts them into JSON format  
- Uploads the JSON file to an S3 bucket  

This simulates backing up or exporting the processed student data.

---

## 🧩 students.json  
This file contains the student dataset used for the project.  
It includes attributes such as:

- `student_id`  
- `student_name`  
- `gender`  
- `grade`  
- `transport`  

---

## 🔎 Interactive Demo (Optional)  
An optional interactive HTML file `index.html` is included to simulate:

- Add, edit, delete students  
- Search, filter by grade  
- Import and export JSON data  

This is a **browser-only demo** and does **not** connect to AWS.

---

## ✔ Requirements Completed  
- DynamoDB table created  
- Data inserted from JSON  
- CRUD operations implemented  
- Grade A query completed  
- Gender count implemented  
- Data exported to S3  
- README included  
- Project structure organized  
- Optionally includes an interactive HTML demo  

---

## 📁 Project Structure  
```text
YourNameStudentDynamoDBProject/
│
├── createTable.py              # Creates DynamoDB table
├── insertFromFile.py           # Inserts JSON data into DynamoDB
├── viewAllStudents.py          # Displays all students
├── updateStudent.py            # Updates student grade
├── deleteStudent.py            # Deletes a student record
├── queryStudents.py            # Grade A query + gender count
├── uploadToS3.py               # Exports DynamoDB data to S3
├── students.json               # Student dataset
├── index.html                  # Interactive demo (optional)
└── README.md                   # Project documentation
