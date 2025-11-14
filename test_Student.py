import pytest

# Import your functions (adjust if your filename is different)
from Student import (
    students_db,
    validate_student_id,
    add_student,
    search_student,
    search_by_class,
    update_student,
    delete_student,
    view_students,
    export_students,
    generate_roll_number
)

# ---------------------------
# FIXTURE → Reset DB before each test
# ---------------------------
@pytest.fixture(autouse=True)
def reset_students_db():
    students_db.clear()
    yield
    students_db.clear()


# ---------------------------
# TEST: Validate Student ID
# ---------------------------
def test_validate_student_id():
    assert validate_student_id("S001") is True
    assert validate_student_id("S120") is True
    assert validate_student_id("A001") is False
    assert validate_student_id("S00A") is False
    assert validate_student_id("001") is False


# ---------------------------
# TEST: Add Student
# ---------------------------
def test_add_student_success():
    result = add_student("S001", "Ali", "10A", phone="12345")
    assert result == "Student Ali added successfully!"
    assert "S001" in students_db
    assert students_db["S001"]["roll_no"] == 1


def test_add_student_invalid_id():
    result = add_student("ABC1", "Ali", "10A")
    assert result == "Error: Invalid student ID format. Use S001, S002 etc."


def test_add_student_duplicate():
    add_student("S001", "Ali", "10A")
    result = add_student("S001", "Ali", "10A")
    assert result == "Error: Student ID already exists."


# ---------------------------
# TEST: Generate Roll Numbers
# ---------------------------
def test_generate_roll_number_increments():
    add_student("S001", "Ali", "10A")
    add_student("S002", "Ahmed", "10A")
    add_student("S003", "Sara", "9B")
    
    assert generate_roll_number("10A") == 3   # two already exist
    assert generate_roll_number("9B") == 2    # one already exists


# ---------------------------
# TEST: View Students
# ---------------------------
def test_view_students():
    add_student("S001", "Ali", "10A")
    result = view_students()
    assert "S001" in result
    assert len(result) == 1


# ---------------------------
# TEST: Search Student by ID
# ---------------------------
def test_search_student_found():
    add_student("S001", "Ali", "10A")
    data = search_student("S001")
    assert data["name"] == "Ali"


def test_search_student_not_found():
    result = search_student("S999")
    assert result == "Error: Student not found."


# ---------------------------
# TEST: Search by Class
# ---------------------------
def test_search_by_class_found():
    add_student("S001", "Ali", "10A")
    add_student("S002", "Ahmed", "10A")
    add_student("S003", "Sara", "9B")

    result = search_by_class("10A")
    assert len(result) == 2
    assert "S001" in result
    assert "S002" in result


def test_search_by_class_not_found():
    result = search_by_class("5C")
    assert result == "No students found in class 5C"


# ---------------------------
# TEST: Update Student
# ---------------------------
def test_update_student():
    add_student("S001", "Ali", "10A")
    result = update_student("S001", name="Ali Raza", phone="555", class_name="12B")

    assert result == "Student information updated successfully."
    assert students_db["S001"]["name"] == "Ali Raza"
    assert students_db["S001"]["phone"] == "555"
    assert students_db["S001"]["class"] == "12B"
    assert students_db["S001"]["roll_no"] == 1  # first student in 12B


def test_update_student_not_found():
    result = update_student("S999", name="New")
    assert result == "Error: Student not found."


# ---------------------------
# TEST: Delete Student
# ---------------------------
def test_delete_student():
    add_student("S001", "Ali", "10A")
    result = delete_student("S001")

    assert result == "Student deleted successfully."
    assert "S001" not in students_db


def test_delete_student_not_found():
    result = delete_student("S555")
    assert result == "Error: Student not found."


# ---------------------------
# TEST: Export File
# ---------------------------
def test_export_students(tmp_path):
    # Add sample
    add_student("S001", "Ali", "10A")

    filename = tmp_path / "export_test.txt"
    result = export_studen_
