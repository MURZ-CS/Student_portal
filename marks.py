# marks.py
marks_db = {}  # key: student_id, value: dict of subject:marks

def add_marks(student_id, subject, marks):
    if student_id not in marks_db:
        marks_db[student_id] = {}
    marks_db[student_id][subject] = marks
    return True, f"Marks added for {student_id} in {subject}"

def view_marks(student_id):
    return marks_db.get(student_id, {})
