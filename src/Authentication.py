from file_managment import read_file
def verify_teacher():
    print("You need to verify yourself as a teacher to add new students")
    teacher_name = input("Enter your name: ")
    teacher_id = input("Enter your id: ")

    datas = read_file("data_files/Teacher.json")
    for data in datas:
        print(data)
        if data['name'] == teacher_name and data['id'] == teacher_id:
            return True
        else:
            return False

if __name__ == "__main__":
    if verify_teacher() == True :
        print("You have gained access")