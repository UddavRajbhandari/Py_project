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

def append_file(file_path, data):
    """
    A function that appends new data to a specified file, ensuring uniqueness based on the file type. 
    Parameters:
        file_path (str): The path to the file where the data will be appended.
        data (Any): The data to be appended to the file.
    Returns:
        None
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError("File not found")
    existing_data = read_file(file_path)
    
    # Ensure data is a list of dictionaries for consistent processing
    if not isinstance(data, list):
        data = [data]
    
    for entry in data:
        # Normalize keys to lowercase for consistency
        normalized_entry = {k.lower(): v for k, v in entry.items()}
        
        # Check for unique identifiers based on the file path
        if file_path.endswith("Student.json"):
            roll_numbers = [item.get("roll_number") for item in existing_data]
            if normalized_entry.get("roll_number") in roll_numbers:
                print(f"Error: A student with roll number '{normalized_entry['roll_number']}' already exists.")
                continue
        elif file_path.endswith("Teacher.json"):
            ids = [item.get("id") for item in existing_data]
            if normalized_entry.get("id") in ids:
                print(f"Error: A teacher with ID '{normalized_entry['id']}' already exists.")
                continue
        
        existing_data.append(entry)
    write_file(file_path, existing_data)

def check_name_key(data):
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
    # write_file("data_files/Student.json", [{"Name":"hari","Roll_number":"45","Marks":{"C":34,"Maths":56,"Python":67},"Address":"kathmandu","Email":"harib@gmail.com","Phone_number":"5453433246"}])
    # append_file("data_files/Student.json", [{"Name":"ram","Roll_number":"43","Marks":{"C":74,"Maths":76,"Python":60},"Address":"kathmandu","Email":"rambhahadu@gmail.com","Phone_number":"9023435234"}])
    write_file("data_files/Teacher.json", [{"name":"hari","subject":"physics","id":45,"address":"bhaktpur","email":"haribil@gmail.com","phone_number":"3454234312"}])
    append_file("data_files/Teacher.json", [{"name":"ram","subject":"Maths","id":245,"address":"Lalitpur","email":"rambil@gmail.com","phone_number":"5654234312"}])
    data = read_file("data_files/Student.json")
    print(data)
