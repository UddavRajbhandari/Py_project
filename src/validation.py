import sys
import os

# Adjust the sys.path to include the parent directory for standalone run
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    sys.path.append(parent_dir)

from src.file_management import *  # Use absolute import
from src.Authentication import authenticate_teacher

def entry(name, id, file_path, new_data): 
    """
    A function that handles the entry of new data into a file after authentication and validation.

    Parameters:
        name (str): The name of the user trying to add new data.
        id (int): The ID of the user.
        file_path (str): The path to the file where the new data will be added.
        new_data (Any): The new data to be appended to the file.

    Returns:
        None
    """
    if authenticate_teacher(name, id):
        if validate(file_path, new_data, read_file(file_path)):
            append_file(file_path, new_data)
            print("Data appended successfully.")
        else:
            print("Validation failed. Data not appended.")
    else:
        print("You need to verify yourself as a teacher to add new students")

if __name__ == "__main__":
    name = input("Enter your name: ")
    id = input("Enter your ID number: ")
    file_path = "data_files/Student.json"
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
    entry(name, id, file_path, new_data)
