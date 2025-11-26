# Student Records CRUD Application using AWS DynamoDB & S3  
**Author:** Ishwariya pandi
**Project:** StudentRecords CRUD Application  

---

## ✧ Overview  
This project implements a complete **Student Records Management System** using AWS services.  
It includes:

⋆ Creating a DynamoDB table  
⋆ Adding JSON student data  
⋆ CRUD functionality (Create, Read, Update, Delete)  
⋆ Querying grade “A” students and gender distribution  
⋆ Exporting processed data to S3  
⋆ Optional interactive HTML demo  

This project demonstrates AWS usage through **Cloud9**, **DynamoDB**, **S3**, and the **Python boto3 library**.

---

## ✧ Technologies Used  
┊ AWS Cloud9  
┊ AWS DynamoDB  
┊ AWS S3  
┊ Python 3  
┊ boto3 SDK  

---

## ✧ Part A: DynamoDB Table Creation  
`createTable.py`  
Creates a DynamoDB table titled **StudentRecords** with:

➤ Partition key: `student_id`  
➤ Data type: Number  

---

## ✧ Part B: Insert Student Data  
`insertFromFile.py` loads `students.json` into DynamoDB.  
Each student entry contains:

— `student_id`  
— `student_name`  
— `gender`  
— `grade`  
— `transport`  

---

## ✧ Part C: CRUD Operations  

### ◦ View Students  
`viewAllStudents.py` retrieves and lists all stored student records.

### ◦ Update Student  
`updateStudent.py` changes the grade of a student identified by `student_id`.

### ◦ Delete Student  
`deleteStudent.py` removes a student record from DynamoDB.

---

## ✧ Part D: Query Functions  
`queryStudents.py` performs two analysis operations:

✦ Displays all students with grade “A” (including A+, A−)  
✦ Counts male and female students  

---

## ✧ Export to S3  
`uploadToS3.py`:

➤ Reads all student records from DynamoDB  
➤ Converts them into JSON  
➤ Uploads the generated file to an S3 bucket  

This simulates data export and backup operations.

---

## ✧ students.json  
This dataset is included in the project and contains:

⊹ Unique student IDs  
⊹ Student names  
⊹ Gender  
⊹ Grade  
⊹ Mode of transport  

This file is used for initial data population.

---

## ✧ Interactive Demo (Optional)  
`index.html` provides a browser-based demonstration supporting:

⋆ Adding students  
⋆ Editing and deleting records  
⋆ Searching and filtering  
⋆ Importing JSON data  
⋆ Exporting data  

It runs entirely in the browser and does not connect to AWS.

---

## ✧ Requirements Completed  
✔ DynamoDB table created  
✔ JSON upload implemented  
✔ CRUD operations functional  
✔ Grade A query performed  
✔ Gender count implemented  
✔ Data exported to S3  
✔ README included  
✔ Optional interactive demo available  

---

## ✧ Project Structure  
```text
YourNameStudentDynamoDBProject/
│
├── createTable.py              ┆ Creates DynamoDB table
├── insertFromFile.py           ┆ Inserts JSON data into DynamoDB
├── viewAllStudents.py          ┆ Displays all students
├── updateStudent.py            ┆ Updates student grade
├── deleteStudent.py            ┆ Deletes student record
├── queryStudents.py            ┆ Grade A query + gender count
├── uploadToS3.py               ┆ Exports DynamoDB data to S3
├── students.json               ┆ Student dataset
├── index.html                  ┆ Optional interactive demo
└── README.md                   ┆ Project documentation
