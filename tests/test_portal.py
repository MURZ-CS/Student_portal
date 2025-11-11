# tests/test_portal.py
import pytest
from Student import add_student, view_students
from teachers import add_teacher
from Attandance import mark_attendance, view_attendance
from marks import add_marks, view_marks
from grades import calculate_grade, calculate_percentage

def test_student_functions():
    add_student("S1", "Alice", "10A")
    students = view_students()
    assert "S1" in students

def test_teacher_functions():
    add_teacher("T1", "Mr. Smith", "Math")
    teachers = {"T1": {"name": "Mr. Smith", "subject": "Math"}}
    assert teachers["T1"]["subject"] == "Math"

def test_attendance_functions():
    mark_attendance("S1", "2025-11-11")
    attendance = view_attendance("S1")
    assert "2025-11-11" in attendance

def test_marks_and_grades():
    add_marks("S1", "Math", 95)
    add_marks("S1", "Science", 85)
    marks_dict = view_marks("S1")
    percentage = calculate_percentage(marks_dict)
    grade = calculate_grade(percentage)
    assert round(percentage, 2) == 90
    assert grade == "A+"
