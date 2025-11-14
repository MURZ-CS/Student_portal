import pytest

# ---- Import all functions from your modules ----
from Student import (
    add_student, view_students, update_student, delete_student,
    search_student_by_id, search_student_by_name, promote_student,
    count_students_by_class
)

from teachers import (
    add_teacher, view_teachers, update_teacher, delete_teacher,
    search_teacher, assign_subject, unassign_subject,
    list_teachers_by_subject
)

from Attandance import (
    mark_attendance, view_attendance, view_attendance_by_student,
    attendance_percentage
)

from marks import (
    add_marks, view_marks, update_marks, delete_marks,
    subject_topper, class_average
)

from grades import (
    calculate_percentage, calculate_grade
)

# ---------------- FIXTURE TO RESET GLOBAL DATA ---------------- #

@pytest.fixture(autouse=True)
def reset_data():
    """
    Automatically runs before each test.
    Clears all global dictionaries inside your modules.
    """
    import Student, teachers, Attandance, marks, grades

    Student.students.clear()
    teachers.teachers.clear()
    Attandance.attendance.clear()
    marks.marks_data.clear()
    grades.marks_reference.clear()

    yield


# ==================== STUDENT TESTS ==================== #

def test_add_student():
    add_student("S1", "Alice", "10A")
    assert "S1" in view_students()


def test_update_student():
    add_student("S1", "Alice", "10A")
    update_student("S1", "Alicia", "10B")
    assert view_students()["S1"]["name"] == "Alicia"


def test_search_student_by_id():
    add_student("S2", "Bob", "9A")
    assert search_student_by_id("S2")["name"] == "Bob"


def test_promote_student():
    add_student("S3", "Charlie", "8A")
    promote_student("S3")
    assert search_student_by_id("S3")["class"] == "9A"


# ==================== TEACHER TESTS ==================== #

def test_add_teacher():
    add_teacher("T1", "Mr. John", "Math")
    assert "T1" in view_teachers()


def test_assign_subject():
    add_teacher("T2", "Ms. Rose", "Science")
    assign_subject("T2", "Biology")
    assert "Biology" in view_teachers()["T2"]["subjects"]


def test_unassign_subject():
    add_teacher("T3", "Mr. Khan", "Physics")
    assign_subject("T3", "Math")
    unassign_subject("T3", "Math")
    assert "Math" not in view_teachers()["T3"]["subjects"]


# ==================== ATTENDANCE TESTS ==================== #

def test_mark_attendance():
    mark_attendance("S1", "2024-01-01", "Present")
    assert view_attendance_by_student("S1")[0]["status"] == "Present"


def test_attendance_percentage():
    mark_attendance("S1", "2024-01-01", "Present")
    mark_attendance("S1", "2024-01-02", "Absent")
    percentage = attendance_percentage("S1")
    assert percentage == 50  # 1/2 days present


# ==================== MARKS TESTS ==================== #

def test_add_marks():
    add_marks("S1", "Math", 88)
    assert view_marks()["S1"]["Math"] == 88


def test_update_marks():
    add_marks("S2", "English", 70)
    update_marks("S2", "English", 92)
    assert view_marks()["S2"]["English"] == 92


def test_delete_marks():
    add_marks("S3", "Physics", 81)
    delete_marks("S3", "Physics")
    assert "Physics" not in view_marks().get("S3", {})


def test_subject_topper():
    add_marks("S1", "Chemistry", 90)
    add_marks("S2", "Chemistry", 95)
    topper = subject_topper("Chemistry")
    assert topper["student_id"] == "S2"


# ==================== GRADES TESTS ==================== #

def test_calculate_percentage():
    # grades module expects marks via its internal marks_reference
    from grades import marks_reference
    marks_reference["S1"] = {"Math": 90, "English": 80, "Science": 70}

    assert calculate_percentage("S1") == 80  # (90+80+70)/3


def test_calculate_grade():
    from grades import marks_reference
    marks_reference["S1"] = {"Math": 95, "English": 96}

    assert calculate_grade("S1") == "A"
