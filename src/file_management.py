import json,sys
import os
# Adjust the sys.path to include the parent directory for standalone run
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    sys.path.append(parent_dir)
def read_file(file_path) -> list:
    """
    Reads a file from the provided file path and returns the data loaded from the file as a list.

    Parameters:
        file_path (str): The path to the file to be read.

    Returns:
        list: The data loaded from the file as a list.
    """
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        try:
            data = json.load(file)
            return data if isinstance(data, list) else []
        except json.JSONDecodeError:
            return []

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
    A function that appends new data to a specified file, ensuring uniqueness based on the file type. 

    Parameters:
        file_path (str): The path to the file where the data will be appended.
        data (Any): The data to be appended to the file.

    Returns:
        None
    """
    existing_data = read_file(file_path)
    if not validate(file_path, data, existing_data):
        print("Validation failed. The data was not appended.")
        return

    if isinstance(data, list):
        for entry in data:
            name = check_name_key(entry)
            if not name:
                print("Error: 'name' or 'Name' key not found in the data.")
                return
        existing_data.extend(data)
    else:
        name = check_name_key(data)
        if not name:
            print("Error: 'name' or 'Name' key not found in the data.")
            return
        existing_data.append(data)
        
    write_file(file_path, existing_data)

def validate(file_path, data, existing_data) -> bool:
    """
    Validates the given data against existing data in a file based on the file path.

    Args:
        file_path (str): The path to the file where the data will be validated.
        data (Union[dict, list]): The data to be validated. It can be a dictionary or a list of dictionaries.
        existing_data (list): The existing data from the file.

    Returns:
        bool: True if the data is valid, False otherwise.
    """
    # Ensure data is a list of dictionaries for consistent processing
    if not isinstance(data, list):
        data = [data]

    # Check for unique identifiers based on the file path
    for entry in data:
        if file_path.endswith("Student.json"):
            if "Roll_number" not in entry:
                print("Error: 'Roll_number' key not found in the data.")
                return False

            roll_number = entry.get("Roll_number")
            if any(item.get("Roll_number") == roll_number for item in existing_data):
                print(f"Error: A student with roll number '{roll_number}' already exists.")
                return False
        elif file_path.endswith("Teacher.json"):
            ids = [str(item.get("id")) for item in existing_data]
            normalized_entry = {k.lower(): v for k, v in entry.items()}
            if str(normalized_entry.get("id")) in ids:
                print(f"Error: A teacher with ID '{normalized_entry['id']}' already exists.")
                return False

    return True


def check_name_key(data) -> str:
    """
    Checks if the 'name' or 'Name' key exists in the data.

    Args:
        data (dict): The data dictionary to check.

    Returns:
        str or None: The value of the 'name' or 'Name' key if found, otherwise None.
    """
    return data.get('name') or data.get('Name')

# Test the functions
if __name__ == "__main__":
    write_file("data_files\Student.json", [{"Name": "hari", "Roll_number": 34, "Marks": {"C": 34, "Maths": 56, "Python": 67}, "Address": "kathmandu", "Email": "harib@gmail.com", "Phone_number": "5453433246"}])
    append_file("data_files\Student.json", {"Name": "ram", "Roll_number": 24, "Marks": {"C": 74, "Maths": 76, "Python": 60}, "Address": "kathmandu", "Email": "rambhahadu@gmail.com", "Phone_number": "9023435234"})
    write_file("data_files\Teacher.json", [{"name": "hari", "subject": "physics", "id": 45, "address": "bhaktpur", "email": "haribil@gmail.com", "phone_number": "3454234312"}])
    append_file("data_files\Teacher.json", {"name": "ram", "subject": "Maths", "id": 35, "address": "Lalitpur", "email": "rambil@gmail.com", "phone_number": "5654234312"})
    data = read_file("data_files\Student.json")
    print(data)
