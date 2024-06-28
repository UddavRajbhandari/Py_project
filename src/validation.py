
from Authentication import authenticate_teacher

def Entry(name,id): 
    # new entry for student must have unique roll number and
    # unque id in case of teacher
    
    if authenticate_teacher(name,id) == True:
        pass
    else:
        assert "You need to verify yourself as a teacher to add new students"

if __name__ == "__main__":
    name = input("Enter your name: ")
    id = input("Enter your ID number: ")
    Entry(name,id)