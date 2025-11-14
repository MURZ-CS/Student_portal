import pytest
from Student import (
    students_db,
    add_student,
    view_students,
    search_student,
    search_by_class,
    update_student,
    delete_student
)

# ----------------- FIXTURE TO RESET DATA ----------------- #
@pytest.fixture(autouse=True)
def reset_data():
    students_db.clear()
    yield


# ==================== SIMPLE TESTS ==================== #

def test_add_student():
    result = add_student("S001", "Alice", "10A")
    assert "added successfully" in result
    assert "S001" in students_db

def test_add_invalid_student():
    result = add_student("X001", "Bob", "10B")
    assert "Invalid student ID" in result

def test_view_students():
    add_student("S002", "Charlie", "9A")
    students = view_students()
    assert "S002" in students
    assert students["S002"]["name"] == "Charlie"

def test_search_student_found():
    add_student("S003", "David", "8A")
    student = search_student("S003")
    assert student["name"] == "David"

def test_search_student_not_found():
    result = search_student("S999")
    assert "not found" in result

def test_search_by_class_found():
    add_student("S004", "Eve", "7A")
    add_student("S005", "Fay", "7A")
    result = search_by_class("7A")
    assert "S004" in result
    assert "S005" in result

def test_search_by_class_not_found():
    result = search_by_class("6B")
    assert "No students found" in result

def test_update_student():
    add_student("S006", "Grace", "6A")
    result = update_student("S006", name="Gracie", phone="123456789")
    assert "updated successfully" in result
    assert students_db["S006"]["name"] == "Gracie"
    assert students_db["S006"]["phone"] == "123456789"

def test_delete_student():
    add_student("S007", "Hank", "5A")
    result = delete_student("S007")
    assert "deleted successfully" in result
    assert "S007" not in students_db
