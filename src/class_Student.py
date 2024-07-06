import sys
import os

# Adjust the sys.path to include the parent directory for standalone run
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    sys.path.append(parent_dir)

from src.file_management import *  # Use absolute import
from src.class_Teacher import Teacher
class Student(Teacher):
    def __init__(self):
        """
        Initializes the Student object with default values.
        """
        super().__init__()
        self.email = ""
        self.phone_number = ""
        self.roll_number = 0
        self.address = ""
        self.marks = {}
        self.name = ""

    def input_data(self):
        """
        Accepts user input for the student object ".
        """       
        print("Enter the information of the student")
        self.name = input("Enter the name of the student: ")
        self.roll_number = int(input("Enter the roll number of the student: "))
        self.marks = {
            "C": int(input("Enter marks in C: ")),
            "Maths": int(input("Enter marks in Maths: ")),
            "Python": int(input("Enter marks in Python: "))
        }
        self.address = input("Enter the address of the student: ")
        self.email = input("Enter the email of the student: ")
        self.phone_number = input("Enter the phone number of the student: ")
    
    def accept(self):
        """
        Accepts user input for the student object and writes it to a JSON file named "Student.json".
        """
        self.input_data()
        if self.check_phone_number(self.phone_number) == True and self.validate_email_domain(self.email) == True:
            data = [{
                "Name":self.name,
                "Roll_number":self.roll_number,
                "Marks":self.marks,
                "Address":self.address,
                "Email":self.email,
                "Phone_number":self.phone_number
              
            }]
            append_file("data_files/Student.json",data)
        else:
            raise ValueError("Invalid email or phone number")
        
            
    
    def display_all(self):
        """
        Display all the details of each student stored in the 'Student.json' file.
        """
        for data in read_file("data_files/Student.json"):
            print(f"Name of the student is {data['Name']}")
            print(f"Email of the student is {data['Email']}")
            print(f"Phone number of the student is {data['Phone_number']}")
            print(f"Roll number of the student is {data['Roll_number']}")
            print(f"marks of the student is {data['Marks']}",end='\n\n')

    def search(self):
        """
        Searches for a student in the 'data_files/Student.json' file based on the provided name.
        If a match is found, it prints the student's details and performs additional calculations.
        If no match is found, it prints a message indicating that no record was found for the student.

        Parameters:
            None

        Returns:
            None
        """
        data = read_file("data_files/Student.json")
        name = input("Enter the name of the student: ")
        for student in data:
            if student['Name'].lower() == name.lower():
                print(f"Name: {student['Name']}, Email: {student['Email']}, Phone: {student['Phone_number']}, Roll number: {student['Roll_number']}, Marks: {student['Marks']}")  
                self.Pass_Fail_Determination(student['Marks'])
                self.Highest_and_lowest_Scores(student['Marks'])
                if self.Pass_Fail_Determination(student['Marks']):
                    self.Percentage(student['Marks'])
                    self.Rank_Calculation(student['Marks'])
                return
        print(f"No record found for student with name {name}")

        

    def Pass_Fail_Determination(self,marks)-> bool:
        """
        Determines if a student has passed or failed based on their marks.

        Args:
            marks (dict): A dictionary containing the marks for each subject.

        Returns:
            bool: True if the student has passed, False otherwise.
        """
       
        passing_marks = 40
        is_pass = all(mark >= passing_marks for mark in marks.values())
        print(f"Pass/Fail: {'Pass' if is_pass else 'Fail'}")
        return is_pass
       
    def Highest_and_lowest_Scores(self,marks)-> None:
        """
        Finds and prints the highest and lowest scores in the given marks dictionary.

        Parameters:
            marks (dict): A dictionary containing the marks for each subject.

        Returns:
            None
        """
       
        highest = max(marks, key=marks.get)
        lowest = min(marks, key=marks.get)
        print(f"Highest Score: {highest} = {marks[highest]}")
        print(f"Lowest Score: {lowest} = {marks[lowest]}")
       
    def Percentage(self,marks)-> None:
        """
        Calculate the percentage of marks obtained by a student.

        Args:
            marks (dict): A dictionary containing the marks for each subject.

        Returns:
            None. Prints the percentage of marks obtained by the student in the format "Percentage: X.XX%".
        """
        total_mark = sum(marks.values())
        number_of_subject = len(marks)
        percentage = (total_mark / (number_of_subject * 100)) * 100
        print(f"Percentage: {round(percentage,2)}%")
        
    
    def Rank_Calculation(self,marks)-> None:
        """
        Calculate the rank of a student based on their marks.

        Args:
            marks (dict): A dictionary containing the marks for each subject.

        Returns:
            None. Prints the rank of the student in the format "Rank: X".
        """
        percentage = (sum(marks.values()) / (len(marks) * 100)) * 100
        if percentage >= 80:
            rank = 'A'
        elif percentage >= 75:
            rank = 'B'
        elif percentage >= 60:
            rank = 'C'
        elif percentage >= 40:
            rank = 'D'
        else:
            rank = 'F'
        print(f"Rank: {rank}")
        
        
    
if __name__ == "__main__":
    
    student = Student()
    # student.accept()
    #student.search() 
    student.display_all()
            
            