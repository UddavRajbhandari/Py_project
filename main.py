# import sys
# import os

# # Adjust the sys.path to include the src directory for standalone run
# if __name__ == "__main__":
#     current_dir = os.path.dirname(os.path.abspath(__file__))
#     sys.path.append(os.path.join(current_dir, "src"))

from src import read_file, authenticate_teacher, AuthenticationError, Student, Teacher, entry

def add_first_teacher():
    teacher = Teacher()
    teacher.accept()
def main():
    
    print("Welcome to the Student data Management Program")
    try:
        # Check if there are any teachers in the system
        teachers = read_file("data_files/Teacher.json")

        if not teachers:
            print("No teachers found. Please add a teacher first.")
            add_first_teacher()
            
        # namme and id of the person should be included in the teacher.json file that to be authenticated for access
        # if teacher.json is empty input the details
        name = input("Enter the name of teacher for access: ")
        teacher_id = input("Enter your ID: ")

        if not authenticate_teacher(name, teacher_id):
            raise AuthenticationError("Authentication failed. Invalid name or ID.")
        
        print("Authentication successful. Welcome!")

        while True:
            print("\nOptions:")
            print("1. Add New Student / Enter student data")
            print("2. Search Student")
            print("3. Display All Students")
            print("4. Add New Teacher")
            print("5. Display All Teachers")
            print("6. Delete Teacher")
            print("7. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                file_path = "data_files/Student.json"
                teacher = Teacher()
                new_data = {
                    "Name": input("Enter the name of the student: "),
                    "Roll_number": int(input("Enter the roll number of the student: ")),
                    "Marks": {
                        "C": int(input("Enter marks in C: ")),
                        "Maths": int(input("Enter marks in Maths: ")),
                        "Python": int(input("Enter marks in Python: "))
                    },
                    "Address": input("Enter the address of the student: "),
                    "Email": input("Enter the email of the student: "),
                    "Phone_number": input("Enter the phone number of the student: ")
                }
                is_email_valid = teacher.validate_email_domain(new_data["Email"])
                is_phone_number_valid = teacher.check_phone_number(new_data["Phone_number"])
                if is_email_valid and is_phone_number_valid:
                    entry(name, teacher_id, file_path, new_data)
                else:
                    if not is_email_valid:
                        print("Invalid email. Student data not added.")
                    if not is_phone_number_valid:
                        print("Invalid phone number. Student data not added.")
     
            elif choice == '2':
                student = Student()
                student.search()
            
            elif choice == '3':
                student = Student()
                student.display_all()
            
            elif choice == '4':
                teacher = Teacher()
                teacher.accept()
            
            elif choice == '5':
                teacher = Teacher()
                teacher.display_teacher()

            
            elif choice == '6':
                teacher = Teacher()
                teacher.delete()
            
            elif choice == '7':
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please select a valid option.")
    
    except AuthenticationError as e:
        print(e)

   
if __name__ == "__main__":
    main()




