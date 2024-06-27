from file_managment import *
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
        if "@" in email:
            return True
        else:
            return False
    
    def check_phone_number(self,phone_number:int)-> bool:
        if len(phone_number) == 10:
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
        if self.check_email_validation(self.email) == True and self.check_phone_number(self.phone_number) == True:
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
        Display all the details of each teacher stored in the 'Teacher.json' file.

        This function reads the 'Teacher.json' file and iterates over each teacher's data.
        It prints the name, subject, email, and phone number of each teacher.

        Parameters:
            self (object): The instance of the Teacher class.

        Returns:
            None
        """
        data = read_file("data_files/Student.json")
        for data in data:
            print(f"Name of the student is {data['name']}")
            print(f"Email of the student is {data['email']}")
            print(f"Phone number of the student is {data['phone_number']}")
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
        name = input("Enter the name of the student")
        for name in data:
            print(f"Name of the student is {data['name']}")
            print(f"Email of the student is {data['email']}")
            print(f"Phone number of the student is {data['phone_number']}")
            print(f"Roll number of the student is {data['roll_number']}")
            print(f"marks of the student is {data['marks']}")
            print(f"percentage of the student is {data['percentage']}")
                
            
    def delete(self):
        """
        Deletes the full detail of the requested person.
        This function does not take any parameters and does not return anything.
        """
        name = input("Enter the name of the Student you want to delete")
        data = read_file("data_files/Student.json")
        for name in data:
            del_data = data.remove(name)
            write_file("data_files/Student.json",del_data)
            
                
if __name__ == "__main__":
    teacher = Teacher()
    teacher.accept()
    teacher.display_all()
    teacher.search()
    teacher.delete()

        
        
        
        
