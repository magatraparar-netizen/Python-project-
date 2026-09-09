students = []

print("Welcome to the Student Data Organizer!")

# main menu
while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

# add student
    if choice == "1":
        print("\nEnter student details:")

        student_id = int(input("Student ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")

        subjects = input("Subjects (comma-separated): ")
        subject_set = set(subjects.split(","))

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "grade": grade,
            "dob": dob,
            "subjects": subject_set
        }
        students.append(student)

        print("\nStudent added successfully!")

        #display all students
    elif choice == "2":
        print("\n--- Display All Students ---")

        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                subjects = ", ".join(student["subjects"])

                print(
                    f"Student ID: {student['id']} | "
                    f"Name: {student['name']} | "
                    f"Age: {student['age']} | "
                    f"Grade: {student['grade']} | "
                    f"Subjects: {subjects}"
                )
                # Update Student Information
    elif choice == "3":
        student_id = int(input("\nEnter Student ID to update: "))

        found = False

        for student in students:
            if student["id"] == student_id:

                print("1. Update Age")
                print("2. Update Subjects")

                update_choice = input("Enter your choice: ")

                if update_choice == "1":
                    student["age"] = int(input("Enter new age: "))
                    print("Age updated successfully!")

                elif update_choice == "2":
                    subjects = input("Enter new subjects (comma-separated): ")
                    student["subjects"] = set(subjects.split(","))
                    print("Subjects updated successfully!")

                else:
                    print("Invalid choice.")

                found = True
                break

        if found == False:
            print("Student not found.")

            # Delete Student
    elif choice == "4":
        student_id = int(input("\nEnter Student ID to delete: "))

        found = False

        for i in range(len(students)):
            if students[i]["id"] == student_id:
                del students[i]
                print("Student deleted successfully!")
                found = True
                break

        if found == False:
            print("Student not found.")

# Display Subjects
    elif choice == "5":
        all_subjects = set()

        for student in students:
            all_subjects.update(student["subjects"])

        print("\n--- Subjects Offered ---")

        if len(all_subjects) == 0:
            print("No subjects available.")
        else:
            for subject in all_subjects:
                print(subject)
                
    # Exit
    elif choice == "6":
        print("\nThank you for using the Student Data Organizer!")
        break
# Invalid choice
    else:
        print("Invalid choice. Please try again.")