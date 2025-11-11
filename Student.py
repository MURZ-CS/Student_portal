# students.py
students_db = {}  # key: student_id, value: dict with name, class

def add_student(student_id, name, class_name):
    if student_id in students_db:
        return False, "Student already exists"
    students_db[student_id] = {"name": name, "class": class_name}
    return True, "Student added successfully"

def view_students():
    return students_db
