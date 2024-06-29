import sys
import os

# Adjust the sys.path to include the parent directory for standalone run
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    sys.path.append(parent_dir)

from src.file_management import *  # Use absolute import
class AuthenticationError(Exception):
    """
    Exception raised when there is an authentication error.
    """
    def __init__(self, message):
        super().__init__(message)
def authenticate_teacher(name, id) -> bool:
    """
    Authenticate a teacher based on their name and ID.

    Args:
        name (str): The name of the teacher.
        id (int): The ID of the teacher.

    Returns:
        bool: True if the teacher is authenticated, False otherwise.

    Raises:
        None

    This function reads the teacher data from the "data_files/Teacher.json" file and checks if the provided name and ID match any of the teachers in the file. If a match is found, the function returns True. Otherwise, it returns False.
    """
    teacher_data = read_file("data_files/Teacher.json")
    for teacher in teacher_data:
        if teacher.get("name").lower() == name.lower() and str(teacher.get("id")) == str(id):
            return True
    return False

def add_new_data()->bool:
    """
    A function that adds new data after authenticating the teacher.
    
    Returns:
        bool: True if authentication is successful, False otherwise.
    """
    name = input("Enter your name: ")
    id = input("Enter your ID number: ")
    try:
        if authenticate_teacher(name, id):
            print("Authentication successful. You may proceed to add new data.")
            return True
        else:
            raise AuthenticationError("Authentication failed. Invalid name or ID.")
    except AuthenticationError as e:
        print(e)
        return False
if __name__ == "__main__":
    add_new_data()