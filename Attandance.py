# Attandance.py

attendance = {}
# Structure:
# attendance = {
#   "S1": {
#       "2025-01-01": "P",
#       "2025-01-02": "A",
#       ...
#    }
# }

VALID_STATUS = ["P", "A", "L", "LEAVE"]  # Present, Absent, Late, Leave


# ------------------------ BASIC ATTENDANCE -------------------------

def mark_attendance(student_id, date, status):
    """Mark attendance for a single student."""
    status = status.upper()

    if status not in VALID_STATUS:
        return "Invalid status. Use P/A/L/LEAVE."

    if student_id not in attendance:
        attendance[student_id] = {}

    if date in attendance[student_id]:
        return "Attendance for this date already marked."

    attendance[student_id][date] = status
    return f"Attendance marked for {student_id} on {date}."


def view_attendance(student_id=None):
    """View all attendance or specific student's attendance."""
    if student_id:
        return attendance.get(student_id, "No records found.")
    return attendance



# -------------------------- UPDATE / DELETE --------------------------

def update_attendance(student_id, date, new_status):
    new_status = new_status.upper()

    if student_id not in attendance:
        return "Student not found."

    if date not in attendance[student_id]:
        return "Attendance for this date not found."

    if new_status not in VALID_STATUS:
        return "Invalid status."

    attendance[student_id][date] = new_status
    return "Attendance updated."


def delete_attendance(student_id, date):
    if student_id not in attendance:
        return "Student not found."

    if date not in attendance[student_id]:
        return "Record not found."

    del attendance[student_id][date]
    return "Attendance record deleted."



# ---------------------------- BULK MARKING ---------------------------

def mark_bulk_attendance(date, student_status_dict):
    """
    Mark attendance for multiple students at once.
    Example input:
    mark_bulk_attendance("2025-05-10", {"S1": "P", "S2": "A", "S3": "L"})
    """
    for sid, status in student_status_dict.items():
        mark_attendance(sid, date, status)

    return "Bulk attendance marked."



# ---------------------- MONTHLY ATTENDANCE --------------------------

def mark_monthly_attendance(student_id, month, status_list):
    """
    Mark attendance for the whole month.
    month format: "2025-05"
    status_list length should match number of days in month.
    """
    import calendar
    year, mon = map(int, month.split("-"))
    days = calendar.monthrange(year, mon)[1]

    if len(status_list) != days:
        return "Status list length does not match days in month."

    for day in range(1, days + 1):
        date = f"{month}-{day:02d}"
        mark_attendance(student_id, date, status_list[day - 1])

    return "Monthly attendance recorded."



# -------------------------- ATTENDANCE REPORTS ----------------------

def view_attendance_by_date(date):
    """Return all students' attendance for a specific date."""
    result = {}
    for sid, records in attendance.items():
        if date in records:
            result[sid] = records[date]
    return result


def view_attendance_by_month(student_id, month):
    """Return all attendance for a student for a given month."""
    if student_id not in attendance:
        return "Student not found."

    return {
        date: status
        for date, status in attendance[student_id].items()
        if date.startswith(month)
    }


def get_full_report(student_id):
    if student_id not in attendance:
        return "Student not found."
    return attendance[student_id]



# ---------------------------- ANALYTICS ------------------------------

def get_attendance_percentage(student_id):
    """Return present percentage."""
    if student_id not in attendance:
        return 0

    records = attendance[student_id].values()
    total = len(records)
    present = list(records).count("P")

    return (present / total) * 100 if total > 0 else 0


def get_stats(student_id):
    """Return present/absent/late/leave counts."""
    if student_id not in attendance:
        return "Student not found."

    records = attendance[student_id].values()

    return {
        "Present": list(records).count("P"),
        "Absent": list(records).count("A"),
        "Late": list(records).count("L"),
        "Leave": list(records).count("LEAVE"),
        "Total Days": len(records)
    }


def class_average_attendance(student_ids):
    """Calculate average attendance % for a class of students."""
    if not student_ids:
        return 0

    total_percentage = sum(get_attendance_percentage(sid) for sid in student_ids)
    return total_percentage / len(student_ids)


def low_attendance_students(threshold=75):
    """Return list of students with attendance below threshold."""
    return [
        sid for sid in attendance
        if get_attendance_percentage(sid) < threshold
    ]


def perfect_attendance_students():
    """Students with 100% presence."""
    return [
        sid for sid in attendance
        if get_attendance_percentage(sid) == 100
    ]


def best_attendance_days(student_id):
    """Days where student was present."""
    if student_id not in attendance:
        return []

    return [date for date, status in attendance[student_id].items() if status == "P"]


def worst_attendance_days(student_id):
    """Days where student was absent."""
    if student_id not in attendance:
        return []

    return [date for date, status in attendance[student_id].items() if status == "A"]

