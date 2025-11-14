import pytest
from Student import (
    students_db, add_student, view_students, update_student,
    delete_student, search_student, search_by_class
)
from teachers import (
    teachers, add_teacher, view_teachers, update_teacher, delete_teacher,
    search_by_name, search_by_subject, search_by_class, search_by_id,
    assign_class, unassign_class, add_subject, remove_subject,
    add_teacher_rating, get_average_rating, count_teachers
)


# ----------------- FIXTURE TO RESET DATA ----------------- #
@pytest.fixture(autouse=True)
def reset_data():
    students_db.clear()
    teachers.clear()
    yield


# ==================== STUDENT TESTS ==================== #

def test_add_student():
    result = add_student("S001", "Alice", "10A", "123456789", "CityX")
    assert "added successfully" in result
    assert "S001" in students_db

def test_invalid_student_id():
    result = add_student("X001", "Bob", "10B")
    assert "Invalid student ID" in result

def test_update_student():
    add_student("S002", "Charlie", "9A")
    result = update_student("S002", name="Charles", phone="987654321")
    assert result == "Student information updated successfully."
    assert students_db["S002"]["name"] == "Charles"
    assert students_db["S002"]["phone"] == "987654321"

def test_delete_student():
    add_student("S003", "David", "8A")
    result = delete_student("S003")
    assert result == "Student deleted successfully."
    assert "S003" not in students_db

def test_search_student():
    add_student("S004", "Eve", "7A")
    result = search_student("S004")
    assert result["name"] == "Eve"
    
def test_search_by_class():
    add_student("S005", "Fay", "6A")
    add_student("S006", "Grace", "6A")
    result = search_by_class("6A")
    # If no students, result is a string → test should fail
    assert isinstance(result, dict), "Expected dict, got string"
    assert "S005" in result
    assert "S006" in result



# ==================== TEACHER TESTS ==================== #

def test_add_teacher():
    result = add_teacher("T001", "Mr. John")
    assert "added successfully" in result
    assert "T001" in teachers

def test_update_teacher():
    add_teacher("T002", "Ms. Rose")
    result = update_teacher("T002", name="Ms. Rosa", subject=["Math"])
    assert result == "Teacher details updated."
    assert teachers["T002"]["name"] == "Ms. Rosa"
    assert "Math" in teachers["T002"]["subject"]

def test_delete_teacher():
    add_teacher("T003", "Mr. Khan")
    result = delete_teacher("T003")
    assert result == "Teacher deleted successfully."
    assert "T003" not in teachers

def test_search_by_name_subject_class():
    add_teacher("T004", "Mrs. Lee", subject=["Science"], assigned_class=["10A"])
    assert "T004" in search_by_name("Mrs. Lee")
    assert "T004" in search_by_subject("Science")
    assert "T004" in search_by_class("10A")

def test_search_by_id():
    add_teacher("T005", "Mr. Tan")
    assert search_by_id("T005")["name"] == "Mr. Tan"

def test_assign_unassign_class():
    add_teacher("T006", "Ms. Kim")
    assign_class("T006", "9B")
    assert "9B" in teachers["T006"]["class"]
    unassign_class("T006", "9B")
    assert "9B" not in teachers["T006"]["class"]

def test_add_remove_subject():
    add_teacher("T007", "Mr. Lee")
    add_subject("T007", "English")
    assert "English" in teachers["T007"]["subject"]
    remove_subject("T007", "English")
    assert "English" not in teachers["T007"]["subject"]

def test_teacher_rating():
    add_teacher("T008", "Ms. Park")
    add_teacher_rating("T008", 4)
    add_teacher_rating("T008", 5)
    avg = get_average_rating("T008")
    assert avg == 4.5

def test_count_teachers():
    add_teacher("T009", "Mr. White")
    add_teacher("T010", "Ms. Black")
    assert count_teachers() == 2
