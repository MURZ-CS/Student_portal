# teachers.py
teachers_db = {}  # key: teacher_id, value: dict with name, subject

def add_teacher(teacher_id, name, subject):
    if teacher_id in teachers_db:
        return False, "Teacher already exists"
    teachers_db[teacher_id] = {"name": name, "subject": subject}
    return True, "Teacher added successfully"

def view_teachers():
    return teachers_db
