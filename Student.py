# =======================
#   STUDENT MANAGEMENT
# =======================

# Global storage for students
students_db = {}

# ----------------------------------------------
# Helper function to validate student ID
# Format: S001, S002, S450 etc.
# ----------------------------------------------
def validate_student_id(student_id):
    if not (student_id.startswith("S") and student_id[1:].isdigit()):
        return False
    return True


# ----------------------------------------------
# Add a new student
# ----------------------------------------------
def add_student(student_id, name, class_name, phone=None, address=None):
    # Validate ID format
    if not validate_student_id(student_id):
        return "Error: Invalid student ID format. Use S001, S002 etc."

    # Prevent duplicates
    if student_id in students_db:
        return "Error: Student ID already exists."

    # Add student with extended info
    students_db[student_id] = {
        "name": name,
        "class": class_name,
        "phone": phone,
        "address": address,
        "roll_no": generate_roll_number(class_name)
    }

    return f"Student {name} added successfully!"


# ----------------------------------------------
# Auto-roll number generator for each class
# ----------------------------------------------
def generate_roll_number(class_name):
    # Count how many students are already in this class
    count = sum(1 for s in students_db.values() if s["class"] == class_name)
    return count + 1


# ----------------------------------------------
# View all students
# ----------------------------------------------
def view_students():
    return students_db


# ----------------------------------------------
# Search student by ID
# ----------------------------------------------
def search_student(student_id):
    if student_id in students_db:
        return students_db[student_id]
    return "Error: Student not found."


# ----------------------------------------------
# Search students by class
# ----------------------------------------------
def search_by_class(class_name):
    result = {sid: data for sid, data in students_db.items() if data["class"] == class_name}
    
    if not result:
        return f"No students found in class {class_name}"
    return result


# ----------------------------------------------
# Update student details
# ----------------------------------------------
def update_student(student_id, name=None, class_name=None, phone=None, address=None):
    if student_id not in students_db:
        return "Error: Student not found."

    # Update only fields provided
    if name:
        students_db[student_id]["name"] = name
    if class_name:
        students_db[student_id]["class"] = class_name
        students_db[student_id]["roll_no"] = generate_roll_number(class_name)  # Update roll no
    if phone:
        students_db[student_id]["phone"] = phone
    if address:
        students_db[student_id]["address"] = address

    return "Student information updated successfully."


# ----------------------------------------------
# Delete a student
# ----------------------------------------------
def delete_student(student_id):
    if student_id not in students_db:
        return "Error: Student not found."

    del students_db[student_id]
    return "Student deleted successfully."


# ----------------------------------------------
# Export students to a file
# ----------------------------------------------
def export_students(filename="students_list.txt"):
    try:
        with open(filename, "w") as f:
            for sid, data in students_db.items():
                f.write(f"{sid} -> {data}\n")
        return f"Students exported to {filename}"
    except:
        return "Error exporting data!"

