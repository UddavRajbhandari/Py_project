import sys
import os

# Adjust the sys.path to include the parent directory
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    sys.path.append(parent_dir)

from src.file_management import *
class Teacher:
    def __init__(self):
        """
        Initializes the Teacher object with default values for name, subject, id, address, email, and phone_number.
        """
        self.name = ""
        self.subject = ""
        self.id = 0
        self.address = ""
        self.email = ""
        self.phone_number = ""
        
    def check_email_validation(self,email:str)-> bool:
        """
        A function to check if the email contains the '@' symbol.

        Parameters:
            email (str): The email address to be validated.

        Returns:
            bool: True if the email contains the '@' symbol, False otherwise.
        """
        if "@" not in email or "." not in email:
            return False
    
        username, domain = email.split("@")
    
        if "." not in domain:
            return False
        
        if not username:
            return False
        
        if not domain.split(".")[0]:
            return False

        return True
    def validate_email_domain(self,email: str) -> bool:
        """
        A function to check if the email is from a valid domain (gmail.com or outlook.com).

        Parameters:
            email (str): The email address to be validated.

        Returns:
            bool: True if the email is from a valid domain, False otherwise.
        """
        if not self.check_email_validation(email):
            print("\n\n")
            print("Invalid email format. Please enter again.")
            return False

        domain = email.split('@')[1]
        if domain != 'gmail.com' and domain != 'outlook.com':
            print("\n\n")
            print("Invalid email domain. Please enter again.")
            return False

        return True
    
    def check_phone_number(self,phone_number:int)-> bool:
        """
        Check if the given phone number is valid.

        Args:
            phone_number (int): The phone number to be checked.

        Returns:
            bool: True if the phone number is valid (10 digits), False otherwise.
        """
        if len(phone_number) == 10 and phone_number.isdigit():
            return True
        else:
            return False
    
    def input_data(self):
        """
        Function to input data for the teacher object including name, subject, id, address, email, and phone number.
        """
        print("Enter the information of the teacher")
        self.name = input("Enter the name of the teacher ")
        self.subject = input("Enter the subject of the teacher ")
        self.id = int(input("Enter the id of the teacher "))
        self.address = input("Enter the address of the teacher ")
        self.email = input("Enter the email of the teacher ")
        self.phone_number = input("Enter the phone number of the teacher ")
        
    def accept(self)-> None:
        """
        Accepts user input for the teacher object and writes it to a JSON file named "Teacher.json".

        This function calls the `input_data` method to prompt the user to enter the name, subject, id, address, email, and phone number of the teacher. It then creates a dictionary with the input data and writes it to the "Teacher.json" file using the `json.dump` function.

        Parameters:
            self (object): The instance of the Teacher class.

        Returns:
            None
        """
        self.input_data()
        if self.validate_email_domain(self.email) == True and self.check_phone_number(self.phone_number) == True:
            data = [{
                "name":self.name,
                "subject":self.subject,
                "id":self.id,
                "address":self.address,
                "email":self.email,
                "phone_number":self.phone_number
            }]
            append_file("data_files/Teacher.json",data)       
        else:
            raise ValueError("Invalid email or phone number")
    def display_all(self):
        """
        Prints the details in student.json file

        This function reads the 'Student.json' file and iterates over each student's data.
        It prints the name ,email, and phone number of each student.

        Parameters:
            self (object): The instance of the Teacher class.

        Returns:
            None
        """
        data = read_file("data_files/Student.json")
        for student in data:
            print(f"Name: {student['Name']}")
            print(f"Email: {student['Email']}")
            print(f"Phone: {student['Phone_number']}",end='\n\n')
    
    def display_teacher(self):
        """
        Prints the details in teacher.json file

        This function reads the 'Teacher.json' file and iterates over each teacher's data.
        It prints the name ,email, and phone number of each teacher.

        Parameters:
            self (object): The instance of the Teacher class.

        Returns:
            None
        """
        data = read_file("data_files/Teacher.json")
        for teacher in data:
            print(f"Name: {teacher['name']}")
            print(f"Email: {teacher['email']}")
            print(f"Phone: {teacher['phone_number']}",end='\n\n')
   
            
    def search(self):
        """
        Placeholder function for searching students.
        Display full detail of the requested person
        Parameters:
            self (object): The instance of the Teacher class.

        Returns:
            None
        """
        data = read_file("data_files/Student.json")
        name = input("Enter the name of the student: ")
        for student in data:
            if student['Name'].lower() == name.lower():
                print(f"Name: {student['Name']}")
                print(f"Email: {student['Email']}")
                print(f"Phone number: {student['Phone_number']}")
                print(f"Roll number: {student['Roll_number']}")
                print(f"Marks: {student['Marks']}")
                return
        print(f"No record found for student with name {name}")

                
            
    def delete(self):
        """
        Deletes the full detail of the requested person.
        This function does not take any parameters and does not return anything.
        """
        data = read_file("data_files/Teacher.json")
        name = input("Enter the name of the teacher to delete: ")
        for teacher in data:
            if teacher['name'].lower() == name.lower():
                data.remove(teacher)
                write_file("data_files/Teacher.json", data)
                print(f"Teacher {name} deleted successfully.")
                return
        print(f"No record found for teacher with name {name}")
            
                
if __name__ == "__main__":
    teacher = Teacher()
    teacher.accept()
    teacher.display_all()
    # teacher.search()
    # teacher.delete()

        
        
        
        
