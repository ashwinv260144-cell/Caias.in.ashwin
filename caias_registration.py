import csv
import os
import re

# CAIAS Student Registration System
# Developed by Ashwin

DATA_FILE = "CAIAS_Students.csv"
FIELDS = ["Name", "Class", "Email", "Roll Number", "Phone"]


def create_database():
    """Create the CSV file with column headings if it does not exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()


def load_students():
    """Read all saved student records."""
    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def valid_email(email):
    """Accept CAIAS college email addresses."""
    return re.fullmatch(
        r"[a-zA-Z0-9._%+-]+@bca\.caias\.in", email
    ) is not None


def valid_roll_number(roll_number):
    """Accept roll numbers such as 26BCA126."""
    return re.fullmatch(r"\d{2}BCA\d{3}", roll_number) is not None


def valid_phone(phone):
    """Check for a 10-digit Indian mobile number."""
    return re.fullmatch(r"[6-9]\d{9}", phone) is not None


def register_student():
    print("\n" + "=" * 48)
    print("              STUDENT REGISTRATION")
    print("=" * 48)

    name = input("Enter student name: ").strip()
    student_class = input("Enter class (BCA/BBA/BCOM): ").strip().upper()
    email = input("Enter college email: ").strip().lower()
    roll_number = input("Enter college roll number (example: 26BCA126): ").strip().upper()
    phone = input("Enter 10-digit phone number: ").strip()

    if not name:
        print("\nError: Student name cannot be empty.")
        return

    if student_class not in {"BCA", "BBA", "BCOM"}:
        print("\nError: Enter BCA, BBA, or BCOM as the class.")
        return

    if not valid_email(email):
        print("\nError: Enter a valid CAIAS email ending in @bca.caias.in.")
        return

    if not valid_roll_number(roll_number):
        print("\nError: Invalid roll number. Example: 26BCA126.")
        return

    if not valid_phone(phone):
        print("\nError: Enter a valid 10-digit Indian mobile number.")
        return

    students = load_students()

    if any(student["Roll Number"] == roll_number for student in students):
        print("\nError: This roll number is already registered.")
        return

    new_student = {
        "Name": name,
        "Class": student_class,
        "Email": email,
        "Roll Number": roll_number,
        "Phone": phone,
    }

    with open(DATA_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writerow(new_student)

    print("\n" + "=" * 48)
    print("          REGISTRATION SUCCESSFUL!")
    print("=" * 48)
    print(f"Student Name : {name}")
    print(f"Class        : {student_class}")
    print(f"Email        : {email}")
    print(f"Roll Number  : {roll_number}")
    print(f"Phone Number : {phone}")
    print("=" * 48)
    print("             Made by Ashwin")
    print("=" * 48)


def view_students():
    students = load_students()

    print("\n" + "=" * 48)
    print("             REGISTERED STUDENTS")
    print("=" * 48)

    if not students:
        print("No students have registered yet.")
        return

    for number, student in enumerate(students, start=1):
        print(f"\nStudent {number}")
        for field in FIELDS:
            print(f"{field:<13}: {student[field]}")

    print("\nTotal registered students:", len(students))


def search_student():
    roll_number = input("\nEnter roll number to search: ").strip().upper()
    students = load_students()

    for student in students:
        if student["Roll Number"] == roll_number:
            print("\nStudent record found:")
            for field in FIELDS:
                print(f"{field:<13}: {student[field]}")
            return

    print("No student found with that roll number.")


def main():
    create_database()

    while True:
        print("\n" + "=" * 48)
        print("         CAIAS STUDENT REGISTRATION SYSTEM")
        print("                    Made by Ashwin")
        print("=" * 48)
        print("1. Register a new student")
        print("2. View all students")
        print("3. Search for a student")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            register_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("\nThank you for using the CAIAS Student Registration System!")
            print("Project developed by Ashwin.")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
