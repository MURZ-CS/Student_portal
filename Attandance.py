# attendance.py
attendance_db = {}  # key: student_id, value: list of dates attended

def mark_attendance(student_id, date):
    if student_id not in attendance_db:
        attendance_db[student_id] = []
    attendance_db[student_id].append(date)
    return True, f"Attendance marked for {student_id} on {date}"

def view_attendance(student_id):
    return attendance_db.get(student_id, [])
