# 🗂️ Student Records CRUD Application – AWS DynamoDB & S3

![DynamoDB](https://img.shields.io/badge/AWS-DynamoDB-4053D6?logo=amazondynamodb&logoColor=white)
![AWS S3](https://img.shields.io/badge/AWS-S3-FF9900?logo=amazonaws&logoColor=white)
![Cloud9](https://img.shields.io/badge/AWS-Cloud9-1F72FF?logo=amazonaws&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-4479A1?logo=python&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

### 🏫 **Arizona State University — AWS Cloud & NoSQL Systems**

---

## 🚀 Overview
A full-scale **AWS DynamoDB project** demonstrating an end-to-end **Student Records Management System**.  
This cloud-based application performs:

- DynamoDB table creation  
- Loading JSON student data  
- Performing CRUD operations  
- Running analytical queries  
- Exporting processed data to S3  
- (Optional) Running an interactive HTML-based CRUD simulator  

This project mirrors enterprise-level NoSQL workflows using AWS.

---

## ⚙️ Technologies & Concepts

- 🗄️ **Database:** AWS DynamoDB  
- ☁️ **Cloud Services:** AWS Cloud9, AWS S3  
- 🐍 **Programming:** Python 3 + boto3  
- 🗃 **Data:** JSON ingestion & export  
- 🔍 **Analytics:** Grade A Query, Gender Count  
- 🛠 **Operations:** Create, Read, Update, Delete  
- 🎨 **Demo:** Interactive local HTML CRUD UI  
- 📤 **Export:** JSON export to S3 bucket  

---

## 🧩 Project Structure (Diagram)

> *(You can replace this with your own diagram image)*

<img width="450" src="https://github.com/user-attachments/assets/6ee581c0-1e57-4f6e-9911-922c3159c89c">

---

## 🧱 Implementation Workflow

### 🔹 Part 1 – DynamoDB Table Creation  
- Created **StudentRecords** table in DynamoDB  
- Primary Key: `student_id` (Number)  
- Defined table configuration and resource provisioning  
📦 **Output:** A NoSQL table ready for CRUD operations.

---

### 🔹 Part 2 – JSON Data Ingestion  
- Loaded **students.json** using `insertFromFile.py`  
- Inserted all student records  
- Ensured correct data types and handling  
📦 **Output:** DynamoDB initialized with student dataset.

---

### 🔹 Part 3 – CRUD Operations  

#### ▸ View Records  
`viewAllStudents.py` scans and prints all records.

#### ▸ Update a Student  
`updateStudent.py` modifies grade values.

#### ▸ Delete a Student  
`deleteStudent.py` removes unwanted records.

📦 **Output:** Full CRUD functionality achieved.

---

### 🔹 Part 4 – Analytical Queries  
Using `queryStudents.py`:

- **Grade A Query:** Fetches students whose grades start with “A”  
- **Gender Summary:** Counts male vs female students  
📤 **Output:** Insightful academic analytics.

---

### 🔹 Part 5 – Export Data to S3  
`uploadToS3.py`:

- Reads all DynamoDB rows  
- Converts dataset into JSON  
- Uploads it to a specified S3 bucket  

📦 **Output:** Cloud-stored JSON export for downstream workflows.

---

### 🔹 Part 6 – Optional Interactive HTML Demo  
`index.html` provides a browser-based simulator with:

- Add, edit, and delete operations  
- Search + grade filtering  
- JSON import/export  
- LocalStorage persistence  

💡 **Pure HTML/JS — runs locally, no AWS required.**

---

## 🗂 Folder Structure

<img width="251" height="296" alt="image" src="https://github.com/user-attachments/assets/5a72dc21-9abc-47fb-b7b4-430d9b61b620" />

---

## 🧭 Logical Overview
- **DynamoDB** stores all student records.  
- **Python boto3** performs all CRUD and export tasks.  
- **S3** serves as the export and storage layer.  
- **Cloud9** hosts the full development environment.  
- **HTML UI** simulates the entire system for demonstration.

---

## 📈 Results Summary

- ✓ CRUD operations functional  
- ✓ Dataset successfully imported  
- ✓ Grade A + Gender queries executed  
- ✓ S3 export task completed  
- ✓ DynamoDB table correctly populated  
- ✓ Optional HTML interface enhances interactivity  

---

## 🧠 Key Learnings

- Understanding NoSQL design with DynamoDB  
- Writing AWS automation scripts using boto3  
- Structuring cloud-based CRUD applications  
- Handling JSON datasets in cloud ecosystems  
- Real-world cloud workflows using Cloud9 + S3  

---

## 🔮 Future Enhancements

- Add **REST API** with Lambda + API Gateway  
- Build **React** or **Streamlit dashboards**  
- Enable **DynamoDB Streams** for real-time updates  
- Implement **scheduled data pipelines**  
- Add **IAM Role-based authorization**  

---
## 📜 License  
This project is released under the **MIT License**.

---

## 🔗 Connect & Portfolio  

👩‍💻 **Author:** *Ishwariya Pandi*  
🎓 Graduate Student — Arizona State University  
📧 **Email:** ipandi1@asu.edu  

🌐 **GitHub Profile:** https://github.com/ishupandi15

---
