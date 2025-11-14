# timetable.py

schedule_db = {}

def add_class_schedule(class_name, day, time, subject, teacher_id):
    schedule_db.setdefault(class_name, {}).setdefault(day, []).append({
        "time": time, "subject": subject, "teacher": teacher_id
    })
    return f"Schedule added for {class_name} on {day}."

def view_schedule(class_name):
    return schedule_db.get(class_name, {})

def view_teacher_schedule(teacher_id):
    result = {}
    for cls, days in schedule_db.items():
        for day, slots in days.items():
            for slot in slots:
                if slot["teacher"] == teacher_id:
                    result.setdefault(cls, {}).setdefault(day, []).append(slot)
    return result
