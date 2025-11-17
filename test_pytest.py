
import pytest
from Student import add_student, view_students, update_student, delete_student, search_student, search_by_class
from teachers import add_teacher, view_teachers, update_teacher, delete_teacher, search_by_name, assign_class
from Attandance import mark_attendance, view_attendance, update_attendance, delete_attendance
from marks import add_marks, view_marks, update_marks, delete_marks, calculate_percentage
from grades import calculate_grade, calculate_gpa, subject_grades

def test_add_view_student():
    add_student("S001", "Alice", "10A", "123456", "Street 1")
    students = view_students()
    assert "S001" in students
    assert students["S001"]["name"] == "Alice"
    assert students["S001"]["class"] == "10A"

def test_update_student():
    add_student("S002", "Bob", "10B", "111", "Addr")
    update_student("S002", name="Bobby")
    assert view_students()["S002"]["name"] == "Bobby"

def test_delete_student():
    add_student("S003", "Charlie", "10C")
    delete_student("S003")
    assert search_student("S003") == "Error: Student not found."


def test_search_by_class():
    add_student("S004", "Daisy", "10A")
    result = search_by_class("10A")
    assert "S004" in result

# ----------------------------
# TEACHER TESTS
# ----------------------------
def test_add_view_teacher():
    add_teacher("T001", "Mr. Smith", ["Math"], ["10A"])
    teachers = view_teachers()
    assert "T001" in teachers
    assert teachers["T001"]["name"] == "Mr. Smith"

def test_update_teacher():
    add_teacher("T002", "Mrs. Jane", ["English"], ["10B"])
    update_teacher("T002", name="Ms. Jane")
    teachers = view_teachers()
    assert teachers["T002"]["name"] == "Ms. Jane"

def test_delete_teacher():
    add_teacher("T003", "Mr. X", ["Science"], ["10C"])
    delete_teacher("T003")
    teachers = view_teachers()
    assert "T003" not in teachers

def test_mark_view_attendance():
    mark_attendance("S001", "2025-11-14", "P")
    records = view_attendance("S001")
    assert records["2025-11-14"] == "P"

def test_update_delete_attendance():
    mark_attendance("S002", "2025-11-14", "A")
    update_attendance("S002", "2025-11-14", "P")
    records = view_attendance("S002")
    assert records["2025-11-14"] == "P"
    delete_attendance("S002", "2025-11-14")
    records = view_attendance("S002")
    assert "2025-11-14" not in records

def test_add_view_marks():
    add_marks("S001", "Math", "midterm", 85)
    add_marks("S001", "Math", "final", 90)
    student_marks = view_marks("S001")
    assert student_marks["Math"]["midterm"] == 85
    assert student_marks["Math"]["final"] == 90

def test_update_delete_marks():
    add_marks("S002", "English", "midterm", 70)
    update_marks("S002", "English", "midterm", 75)
    student_marks = view_marks("S002")
    assert student_marks["English"]["midterm"] == 75
    delete_marks("S002", "English", "midterm")
    assert "midterm" not in student_marks["English"]

def test_calculate_percentage():
    add_marks("S003", "Science", "midterm", 80)
    add_marks("S003", "Science", "final", 90)
    perc = calculate_percentage("S003")
    assert round(perc, 2) == 85.0

def test_calculate_grade():
    assert calculate_grade(95) == "A+"
    assert calculate_grade(82) == "A"
    assert calculate_grade(76) == "B+"
    assert calculate_grade(61) == "B"
    assert calculate_grade(45) == "D"
    assert calculate_grade(30) == "F"

def test_subject_grades():
    add_marks("S004", "Math", "midterm", 88)
    add_marks("S004", "Math", "final", 92)
    add_marks("S004", "Physics", "midterm", 70)
    add_marks("S004", "Physics", "final", 72)
    grades = subject_grades("S004")
    assert grades["Math"] == "A+"
    assert grades["Physics"] == "B+"

def test_calculate_gpa():
    add_marks("S005", "Math", "midterm", 85)
    add_marks("S005", "Math", "final", 90)
    add_marks("S005", "Physics", "midterm", 70)
    add_marks("S005", "Physics", "final", 72)
    gpa = calculate_gpa("S005")
    assert round(gpa, 2) == 3.5

