# teachers.py
import hashlib

teachers = {}  
# Structure:
# teachers = {
#   "T1": {
#       "name": "...",
#       "subject": ["Math", "Physics"],
#       "class": ["10A"],
#       "password": "<hashed>",
#       "ratings": [4,5,5],
#   }
# }


# ----------------------------- UTILITY ------------------------------

def hash_password(password: str) -> str:
    """Hash password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()



# --------------------- BASIC CRUD OPERATIONS ------------------------

def add_teacher(t_id, name, subject=None, assigned_class=None, password="1234"):
    """Add a new teacher with default password."""
    if t_id in teachers:
        return f"Teacher with ID {t_id} already exists."

    teachers[t_id] = {
        "name": name,
        "subject": subject if subject else [],
        "class": assigned_class if assigned_class else [],
        "password": hash_password(password),
        "ratings": [],
    }
    return f"Teacher {name} added successfully."


def view_teachers():
    """Return full teacher dictionary."""
    return teachers


def update_teacher(t_id, name=None, subject=None, assigned_class=None):
    """Update teacher details."""
    if t_id not in teachers:
        return "Invalid teacher ID"

    if name:
        teachers[t_id]["name"] = name

    if subject:
        teachers[t_id]["subject"] = subject

    if assigned_class:
        teachers[t_id]["class"] = assigned_class

    return "Teacher details updated."


def delete_teacher(t_id):
    """Remove a teacher."""
    if t_id not in teachers:
        return "Teacher ID not found."

    del teachers[t_id]
    return "Teacher deleted successfully."



# ----------------------------- SEARCH -------------------------------

def search_by_name(name):
    return {tid: data for tid, data in teachers.items() if data["name"].lower() == name.lower()}


def search_by_subject(subject):
    return {tid: data for tid, data in teachers.items() if subject in data["subject"]}


def search_by_class(class_name):
    return {tid: data for tid, data in teachers.items() if class_name in data["class"]}


def search_by_id(t_id):
    return teachers.get(t_id, "Teacher not found")



# --------------------------- AUTH SYSTEM ----------------------------

def register_teacher(t_id, name, password):
    """Register new teacher with login capability."""
    if t_id in teachers:
        return "Teacher ID already registered."

    teachers[t_id] = {
        "name": name,
        "subject": [],
        "class": [],
        "password": hash_password(password),
        "ratings": [],
    }
    return "Registration successful."


def login_teacher(t_id, password):
    """Teacher login with password verification."""
    if t_id not in teachers:
        return "Teacher not found."

    if teachers[t_id]["password"] == hash_password(password):
        return "Login successful."
    return "Incorrect password."


def change_teacher_password(t_id, old_password, new_password):
    if t_id not in teachers:
        return "Invalid ID."

    if teachers[t_id]["password"] != hash_password(old_password):
        return "Old password incorrect."

    teachers[t_id]["password"] = hash_password(new_password)
    return "Password changed successfully."



# ---------------------- CLASS MANAGEMENT ----------------------------

def assign_class(t_id, class_name):
    """Assign a teacher to a class."""
    if t_id not in teachers:
        return "Invalid teacher ID"

    if class_name not in teachers[t_id]["class"]:
        teachers[t_id]["class"].append(class_name)

    return f"Class {class_name} assigned to {teachers[t_id]['name']}."


def unassign_class(t_id, class_name):
    """Remove assigned class."""
    if t_id not in teachers:
        return "Invalid teacher ID"

    if class_name in teachers[t_id]["class"]:
        teachers[t_id]["class"].remove(class_name)
        return "Class unassigned."
    return "Class not assigned."


def view_assigned_classes(t_id):
    if t_id not in teachers:
        return "Invalid teacher ID"
    return teachers[t_id]["class"]



# ---------------------- SUBJECT MANAGEMENT --------------------------

def add_subject(t_id, subject):
    if t_id not in teachers:
        return "Invalid teacher ID"

    if subject not in teachers[t_id]["subject"]:
        teachers[t_id]["subject"].append(subject)

    return "Subject added."


def remove_subject(t_id, subject):
    if t_id not in teachers:
        return "Invalid teacher ID"

    if subject in teachers[t_id]["subject"]:
        teachers[t_id]["subject"].remove(subject)
        return "Subject removed."
    return "Subject not found."



# ---------------------- RATINGS / ANALYTICS -------------------------

def add_teacher_rating(t_id, rating):
    """Add a rating (1–5)."""
    if t_id not in teachers:
        return "Invalid teacher ID"

    if not (1 <= rating <= 5):
        return "Rating must be between 1 and 5."

    teachers[t_id]["ratings"].append(rating)
    return "Rating added."


def get_average_rating(t_id):
    """Return avg rating of the teacher."""
    if t_id not in teachers:
        return "Invalid teacher ID"

    r = teachers[t_id]["ratings"]
    if not r:
        return "No ratings yet."

    return sum(r) / len(r)



# ------------------------ STATISTICS --------------------------------

def count_teachers():
    return len(teachers)

