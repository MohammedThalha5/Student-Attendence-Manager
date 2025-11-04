# Student Attendance Tracker (Code Squad)

import mysql.connector
from datetime import date
from tabulate import tabulate

# ------------------ DATABASE CONNECTION ------------------
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",            
        password="mysql",
        database="attendance_db"
    )
    mycursor = mydb.cursor()
except mysql.connector.Error as err:
    print(f" Database connection failed: {err}")
    exit()

# ------------------ FUNCTIONS ------------------

def add_student():
    print("\n ADD NEW STUDENT")
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")

    sql = "INSERT INTO attendance_records (student_id, student_name, date, status) VALUES (%s, %s, %s, %s)"
    val = (student_id, student_name, None, None)
    mycursor.execute(sql, val)
    mydb.commit()
    print(" Student added successfully!")


def mark_attendance():
    print("\n MARK ATTENDANCE")
    student_id = input("Enter Student ID: ")

    # Check if student exists
    mycursor.execute("SELECT student_name FROM attendance_records WHERE student_id=%s LIMIT 1", (student_id,))
    result = mycursor.fetchone()
    if not result:
        print(" Student not found! Please add student first.")
        return

    student_name = result[0]
    today = date.today()
    status = input("Enter Status (Present/Absent): ").capitalize()

    sql = "INSERT INTO attendance_records (student_id, student_name, date, status) VALUES (%s, %s, %s, %s)"
    val = (student_id, student_name, today, status)
    mycursor.execute(sql, val)
    mydb.commit()
    print(f" Attendance marked for {student_name} on {today}!")


def view_all_records():
    print("\n ALL ATTENDANCE RECORDS")
    mycursor.execute("SELECT student_id, student_name, date, status FROM attendance_records WHERE date IS NOT NULL ORDER BY date DESC")
    records = mycursor.fetchall()

    if not records:
        print(" No attendance records found.")
        return

    print(tabulate(records, headers=["Student ID", "Name", "Date", "Status"], tablefmt="grid"))


def view_individual_report():
    print("\n INDIVIDUAL STUDENT REPORT")
    student_id = input("Enter Student ID: ")

    mycursor.execute("SELECT student_name FROM attendance_records WHERE student_id=%s LIMIT 1", (student_id,))
    result = mycursor.fetchone()
    if not result:
        print(" Student not found!")
        return

    student_name = result[0]
    mycursor.execute("SELECT date, status FROM attendance_records WHERE student_id=%s AND date IS NOT NULL", (student_id,))
    records = mycursor.fetchall()

    if not records:
        print(" No attendance data found for this student.")
        return

    total_days = len(records)
    present_days = sum(1 for r in records if r[1] == "Present")
    percentage = (present_days / total_days) * 100

    print(f"\n Attendance Report for {student_name} ({student_id})")
    print(tabulate(records, headers=["Date", "Status"], tablefmt="grid"))
    print(f"\n Total Days: {total_days}")
    print(f" Present Days: {present_days}")
    print(f" Attendance Percentage: {percentage:.2f}%\n")


# ------------------ MAIN MENU ------------------
def main():
    while True:
        print("\n STUDENT ATTENDANCE TRACKER (Code Squad)")
        print("----------------------------------------")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View All Attendance Records")
        print("4. View Individual Report")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            mark_attendance()
        elif choice == '3':
            view_all_records()
        elif choice == '4':
            view_individual_report()
        elif choice == '5':
            print("\n Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.")

# ------------------ START PROGRAM ------------------
if __name__ == "__main__":
    main()
