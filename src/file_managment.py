import json
import os

def read_file(file_path) -> dict:
    """
    Reads a file from the provided file path and returns the data loaded from the file as a dictionary.

    Parameters:
        file_path (str): The path to the file to be read.

    Returns:
        dict: The data loaded from the file as a dictionary.
    """
    if not os.path.exists(file_path):
        return {}
    with open(file_path, "r") as file:
        data = json.load(file)
        return data

def write_file(file_path, data) -> None:
    """
    Write the given data to a file at the specified file path.

    Parameters:
        file_path (str): The path to the file where the data will be written.
        data (Any): The data to be written to the file.

    Returns:
        None
    """
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def append_file(file_path, data) -> None:
    """
    Appends the given data to a file at the specified file path.

    Args:
        file_path (str): The path to the file where the data will be appended.
        data (Any): The data to be appended to the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.

    Returns:
        None
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError("File not found")
    existing_data = read_file(file_path)
    # If the existing data is not a list, convert it to a list
    if not isinstance(existing_data, list):
        existing_data = [existing_data]
    existing_data.append(data)
    write_file(file_path, existing_data)

# Test the functions
if __name__ == "__main__":
    write_file("data_files/Student.json", [{"name": "shyam", "subject": "english", "id": 34, "address": "lalitpur", "email": "shyambh@gmail.com", "phone_number": "5453433245"}])
    append_file("data_files/Student.json", {"name": "hari", "subject": "math", "id": 35, "address": "kathmandu", "email": "harib@gmail.com", "phone_number": "5453433246"})
    data = read_file("data_files/Student.json")
    print(data)
