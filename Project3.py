# Student Data Organizer

def display_welcome():
    print("="*50)
    print("Welcome to the Student Data Organizer!")
    print("="*50)
    print("This program allows you to manage student records.")
    print("You can:")
    print(" - Add new students with details like name, age, grade, subjects, etc.")
    print(" - Display all student records in a formatted way.")
    print(" - Update mutable information (age, grade, subjects).")
    print(" - Delete a student record using their Student ID.")
    print(" - View all unique subjects offered across students.")
    print(" - Exit the program anytime.\n")
    print("Let's get started!\n")

def display_menu():
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

# Store all student records in a list
student_records = []

def add_student():
    try:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        grade = input("Enter Grade: ")
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")
        subjects = input("Enter Subjects (comma-separated): ").split(",")

        # Tuple for unchangeable info
        student_key = (student_id, dob)

        # Dictionary for mutable info
        student_data = {
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": [s.strip() for s in subjects]
        }

        # Append as dictionary with tuple key
        record = {student_key: student_data}
        student_records.append(record)

        print("\nStudent added successfully!")
    except ValueError:
        print("Invalid input! Please enter correct data types.")

def display_all_students():
    if not student_records:
        print("\nNo student records found.")
        return
    print("\n--- Display All Students ---")
    for record in student_records:
        for (sid, dob), details in record.items():
            print(f"Student ID: {sid} | Name: {details['name']} | Age: {details['age']} | "
                  f"Grade: {details['grade']} | DOB: {dob} | Subjects: {', '.join(details['subjects'])}")

def update_student():
    sid = int(input("Enter Student ID to update: "))
    for record in student_records:
        for (student_id, dob), details in record.items():
            if student_id == sid:
                print("\nWhat do you want to update?")
                print("1. Age")
                print("2. Grade")
                print("3. Subjects")
                choice = input("Enter your choice: ")
                if choice == "1":
                    details["age"] = int(input("Enter new Age: "))
                elif choice == "2":
                    details["grade"] = input("Enter new Grade: ")
                elif choice == "3":
                    details["subjects"] = input("Enter new Subjects (comma-separated): ").split(",")
                print("Student record updated successfully!")
                return
    print("Student not found.")

def delete_student():
    sid = int(input("Enter Student ID to delete: "))
    for i, record in enumerate(student_records):
        for (student_id, dob) in record.keys():
            if student_id == sid:
                del student_records[i]
                print("Student record deleted successfully!")
                return
    print("Student not found.")

def display_subjects():
    subjects = set()
    for record in student_records:
        for (sid, dob), details in record.items():
            subjects.update(details["subjects"])
    if subjects:
        print("\nSubjects Offered:", ", ".join(subjects))
    else:
        print("\nNo subjects found.")

# Main program
display_welcome()

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_all_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        display_subjects()
    elif choice == "6":
        print("\n=======================================")
        print("Thank you for using the Student Data Organizer.")
        print("Program closed successfully. Goodbye!")
        print("=======================================\n")
        break
    else:
        print("Invalid choice! Please try again.")
