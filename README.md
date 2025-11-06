# Student-Attendence-Manager
Python Project
# 🎓 Student Attendance Tracker

## 📘 Project Overview
The **Student Attendance Tracker** is a Python-based application integrated with a **MySQL database** to manage and record student attendance efficiently.  
It allows adding student details, marking daily attendance, viewing attendance records, and generating attendance reports — all through a simple, menu-driven interface.

---

## 🧑‍💻 Team Information
**Team Name:** 🧠 Code Squad

| Reg. No     | Name             |
|--------------|------------------|
| 25BDS0206    | Mohammed Thalha  |
| 25BDS0193    | Nitin Krishna    |
| 25BDS0195    | Prajanth R       |
| 25BDS0135    | Shanmugesh       |
| 25BDS0154    | Nikhil           |

---

## 🧩 Features
✅ Add new students to the system  
✅ Mark daily attendance (Present/Absent)  
✅ View all attendance records  
✅ View individual student attendance reports  
✅ Calculate attendance percentage  
✅ Stores all data securely in a MySQL database  

---

## 🗄️ Database Design

**Database Name:** `attendance_db`  
**Table Name:** `attendance_records`

| Field Name    | Type         | Description                  |
|----------------|--------------|------------------------------|
| id             | INT (PK, AUTO_INCREMENT) | Unique ID for each record |
| student_id     | VARCHAR(10)  | Student Roll Number          |
| student_name   | VARCHAR(50)  | Name of Student              |
| date           | DATE         | Date of Attendance           |
| status         | VARCHAR(10)  | Present / Absent             |

---

## ⚙️ Tools and Technologies Used
- **Python 3.x**
- **MySQL** (Database)
- **mysql-connector-python** (Library)
- **datetime** (Date handling)
- **tabulate** (Optional, for table formatting)

---

## 📦 Installation and Setup

### 1️⃣ Install Required Libraries
```bash
pip install mysql-connector-python tabulate

