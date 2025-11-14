import pytest
from marks import (
    marks,
    add_marks,
    view_marks,
    update_marks,
    delete_marks,
    view_subject_marks,
    calculate_total_marks,
    calculate_percentage,
    best_subject,
    weakest_subject,
    topper,
    class_average,
    subject_wise_grade,
    generate_full_report
)

# ----------------- FIXTURE TO RESET DATA ----------------- #
@pytest.fixture(autouse=True)
def reset_marks():
    marks.clear()
    yield

# ==================== TESTS ==================== #

def test_add_marks():
    res = add_marks("S001", "Math", "midterm", 85)
    assert "Marks added" in res
    assert marks["S001"]["Math"]["midterm"] == 85

    res_invalid_exam = add_marks("S001", "Math", "test", 50)
    assert "Invalid exam type" in res_invalid_exam

    res_invalid_score = add_marks("S001", "Math", "final", 150)
    assert "Marks must be between 0 and 100" in res_invalid_score

def test_view_marks():
    add_marks("S001", "Math", "midterm", 90)
    assert view_marks("S001") == marks
    assert "S002" not in view_marks()

def test_update_marks():
    add_marks("S001", "Math", "midterm", 85)
    res = update_marks("S001", "Math", "midterm", 95)
    assert res == "Marks updated successfully."
    assert marks["S001"]["Math"]["midterm"] == 95

    res_invalid = update_marks("S002", "Math", "midterm", 50)
    assert res_invalid == "Student not found."

def test_delete_marks():
    add_marks("S001", "Math", "midterm", 85)
    res_exam = delete_marks("S001", "Math", "midterm")
    assert res_exam == "midterm deleted."
    assert "midterm" not in marks["S001"]["Math"]

    add_marks("S001", "Math", "final", 90)
    res_subject = delete_marks("S001", "Math")
    assert res_subject == "Subject deleted."
    assert "Math" not in marks["S001"]

def test_view_subject_marks():
    add_marks("S001", "Physics", "midterm", 80)
    subj = view_subject_marks("S001", "Physics")
    assert subj["midterm"] == 80

    assert view_subject_marks("S002", "Math") == "Student not found."

def test_calculate_total_and_percentage():
    add_marks("S001", "Math", "midterm", 80)
    add_marks("S001", "Math", "final", 90)
    add_marks("S001", "Physics", "midterm", 70)
    assert calculate_total_marks("S001") == 240
    assert calculate_percentage("S001") == pytest.approx((80+90+70)/300*100)

def test_best_and_weakest_subject():
    add_marks("S001", "Math", "midterm", 80)
    add_marks("S001", "Physics", "midterm", 60)
    best, best_avg = best_subject("S001")
    weak, weak_avg = weakest_subject("S001")
    assert best == "Math"
    assert weak == "Physics"

def test_topper_and_class_average():
    add_marks("S001", "Math", "midterm", 80)
    add_marks("S002", "Math", "midterm", 90)
    top_student, top_score = topper(["S001", "S002"])
    avg = class_average(["S001", "S002"])
    assert top_student == "S002"
    assert avg == pytest.approx((80+90)/2)

def test_subject_wise_grade():
    add_marks("S001", "Math", "midterm", 95)
    add_marks("S001", "Physics", "midterm", 70)
    grades = subject_wise_grade("S001")
    assert grades["Math"] == "A+"
    assert grades["Physics"] == "B+"

def test_generate_full_report():
    add_marks("S001", "Math", "midterm", 80)
    add_marks("S001", "Physics", "midterm", 70)
    report = generate_full_report("S001")
    assert report["Marks"] == marks["S001"]
    assert report["Best Subject"][0] == "Math"
    assert report["Weakest Subject"][0] == "Physics"
