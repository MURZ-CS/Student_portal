# test_school_system.py
import pytest

# Import modules
from Student import add_student, view_students, update_student, delete_student, search_student, search_by_class
from teachers import add_teacher, view_teachers, update_teacher, delete_teacher, search_by_name, assign_class, add_subject, add_teacher_rating, get_average_rating, count_teachers
from Attandance import mark_attendance, view_attendance, update_attendance, delete_attendance, get_attendance_percentage
from marks import add_marks, view_marks, calculate_percentage, best_subject, weakest_subject
from grades import calculate_grade, calculate_gpa, rank_students

# ----------------------
# STUDENT TEST CASES
# ----------------------
def test_add_view_update_delete_student():
    # Add
    res = add_student("S001", "Alice", "10A")
    assert "added" in res.lower()

    # View
    students = view_students()
    assert "S001" in students

    # Update
    res = update_student("S001", name="Alice B")
    assert "updated" in res.lower()
    assert view_students()["S001"]["name"] == "Alice B"

    # Search
    student = search_student("S001")
    assert student["name"] == "Alice B"

    # Delete
    res = delete_student("S001")
    assert "deleted" in res.lower()
    assert "S001" not in view_students()

# ----------------------
# TEACHER TEST CASES
# ----------------------
def test_teacher_crud_and_subject():
    # Add
    res = add_teacher("T001", "Mr. Smith", ["Math"], ["10A"])
    assert "added" in res.lower()

    # View
    teachers = view_teachers()
    assert "T001" in teachers

    # Update
    res = update_teacher("T001", name="Mr. S")
    assert "updated" in res.lower()
    assert teachers["T001"]["name"] == "Mr. S"

    # Assign class
    assign_class("T001", "10B")
    assert "10B" in teachers["T001"]["class"]

    # Add subject
    add_subject("T001", "Physics")
    assert "Physics" in teachers["T001"]["subject"]

    # Rating
    add_teacher_rating("T001", 4)
    add_teacher_rating("T001", 5)
    avg = get_average_rating("T001")
    assert avg == 4.5

    # Count
    count = count_teachers()
    assert count >= 1

    # Delete
    delete_teacher("T001")
    assert "T001" not in view_teachers()

# ----------------------
# ATTENDANCE TEST CASES
# ----------------------
def test_attendance_mark_view_update_delete():
    mark_attendance("S002", "2025-11-14", "P")
    att = view_attendance("S002")
    assert att["2025-11-14"] == "P"

    # Update
    update_attendance("S002", "2025-11-14", "A")
    att = view_attendance("S002")
    assert att["2025-11-14"] == "A"

    # Attendance %
    perc = get_attendance_percentage("S002")
    assert perc == 0  # 1 day absent → 0% present

    # Delete
    delete_attendance("S002", "2025-11-14")
    att = view_attendance("S002")
    assert att == {}

# ----------------------
# MARKS TEST CASES
# ----------------------
def test_marks_operations():
    add_marks("S003", "Math", "midterm", 80)
    add_marks("S003", "Math", "final", 90)
    add_marks("S003", "English", "midterm", 70)

    marks = view_marks("S003")
    assert "Math" in marks
    assert marks["Math"]["midterm"] == 80

    # Calculate %
    perc = calculate_percentage("S003")
    expected = (80 + 90 + 70) / 3
    assert perc == expected

    # Best / Weakest
    best, weak = best_subject("S003")
    assert best == "Math"
    assert weak == "English"

# ----------------------
# GRADES TEST CASES
# ----------------------
def test_grades_functions():
    grade = calculate_grade(85)
    assert grade == "A"

    gpa = calculate_gpa("S003")
    assert gpa > 0

    ranking = rank_students(["S003"])
    assert ranking[0][0] == "S003"

# ----------------------
# RUN ALL
# ----------------------
if __name__ == "__main__":
    pytest.main()
