
from Teacher import Teacher
from file_managment import *
class Student(Teacher):
    def __init__(self):
        """
        Initializes the Student object with default values.
        """
        self.email = ""
        self.phone_number = ""
        self.roll_number = 0
        self.address = ""
        self.marks = 0
        self.name = ""
        
 

    def input_data(self):
        """
        Accepts user input for the student object and writes it to a JSON file named "Student.json".
        """
        print("Enter the information of the student ")
        self.name = input("Enter the name of the student ")
        self.roll_number = input("Enter the roll no of the student ")
        self.marks = int(input("Enter the marks of the student "))
        self.address = input("Enter the address of the student ")
        self.email = input("Enter the email of the student ")
        self.phone_number = input("Enter the phone number of the student ")
    
    def accept(self):
        """
        Accepts user input for the student object and writes it to a JSON file named "Student.json".
        """
        self.input_data()
        data = [{
            "name":self.name,
            "roll_number":self.roll_number,
            "marks":self.marks,
            "address":self.address,
            "email":self.email,
            "phone_number":self.phone_number
        }]
        append_file("data_files/Student.json",data)
            
    
    def display_all(self):
        """
        Display all the details of each student stored in the 'Student.json' file.
        """
        # use teacher class for display
        Teacher.display_all(self)
    def search(self):
        """
        Placeholder function for searching students.
        Display full detail of the requested person
        """
        data = read_file("data_files/Student.json")
        name = input("Enter the name of the student")
        for data['name'] in data:
            print(f"Name of the student is {data['name']}")
            print(f"Email of the student is {data['email']}")
            print(f"Phone number of the student is {data['phone_number']}")
            print(f"Roll number of the student is {data['roll_number']}")
            print(f"marks of the student is {data['marks']}")
            print(f"percentage of the student is {data['percentage']}")
    def Pass_Fail_Determination(self):
        """
        Pass or Fail determination
        """
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")
    def Highest_and_lowest_Scores(self):
        """
        Highest and lowest scores
        """
        if self.marks > 80:
            print("Highest Score")
        elif self.marks > 50 and self.marks < 80:
            print("Average Score")
        else:
            print("Lowest Score")
    def Percentage(self):
        mark = self.marks
        percentage = sum(mark)/len(mark)
        
    
    def Rank_Calculation(self):
        """
        Rank Calculation based on percentage
        """
        per = self.Percentage()
        
    
if __name__ == "__main__":
    student = Student()
    student.accept()
    student.display_all() 
            
            