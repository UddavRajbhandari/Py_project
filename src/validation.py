
from Authentication import verify_teacher

def Entry(): 
    # new entry for student must have unique roll number and
    # unque id in case of teacher
    if verify_teacher() == True:
        pass
    else:
        assert "You need to verify yourself as a teacher to add new students"

if __name__ == "__main__":
    Entry()