from file_managment import read_file

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
        if teacher.get("name") == name and str(teacher.get("id")) == id:
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
            # Add functionality for adding new data
            # For example:
            new_data = input("Enter the new data to add: ")
            # Append this new data to the appropriate file
            # append_file("data_files/Student.json", json.loads(new_data))
            return True
        else:
            raise AuthenticationError("Authentication failed. Invalid name or ID.")
    except AuthenticationError as e:
        print(e)
        return False
if __name__ == "__main__":
    add_new_data()