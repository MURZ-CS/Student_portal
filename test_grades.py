import pytest
from grades import (
    calculate_grade,
    get_grade_point,
    calculate_gpa,
    calculate_cgpa,
    classify_result,
    calculate_weighted_marks,
    rank_students,
    generate_transcript,
    subject_grades
)
from marks import marks, calculate_percentage

# ----------------- FIXTURE TO RESET DATA ----------------- #
@pytest.fixture(autouse=True)
def reset_marks():
    marks.clear()
    yield

# ==================== MOCK DATA ==================== #
def setup_mock_data():
    marks["S001"] = {
        "Math": {"midterm": 80, "final": 90},
        "Physics": {"midterm": 70, "final": 60}
    }
    marks["S002"] = {
        "Math": {"midterm": 50, "final": 60},
        "Physics": {"midterm": 40, "final": 50}
    }

# ==================== TESTS ==================== #

def test_calculate_grade():
    assert calculate_grade(95) == "A+"
    assert calculate_grade(85) == "A"
    assert calculate_grade(72) == "B+"
    assert calculate_grade(35) == "F"

def test_get_grade_point():
    assert get_grade_point("A+") == 4.0
    assert get_grade_point("C") == 2.0
    assert get_grade_point("F") == 0.0
    assert get_grade_point("Unknown") == 0.0

def test_calculate_gpa():
    setup_mock_data()
    gpa = calculate_gpa("S001")
    assert round(gpa, 2) == 3.15  # (Math: 3.7 + Physics: 2.6)/2 ≈ 3.15

def test_calculate_cgpa():
    gpa_list = [3.0, 3.5, 4.0]
    cgpa = calculate_cgpa(gpa_list)
    assert cgpa == 3.5

def test_classify_result():
    assert classify_result(80) == "Distinction"
    assert classify_result(65) == "Merit"
    assert classify_result(50) == "Pass"
    assert classify_result(30) == "Fail"

def test_calculate_weighted_marks():
    setup_mock_data()
    weighted = calculate_weighted_marks("S001")
    assert weighted["Math"] == 86.0  # 80*0.4 + 90*0.6
    assert weighted["Physics"] == 64.0  # 70*0.4 + 60*0.6

def test_rank_students():
    setup_mock_data()
    ranking = rank_students(["S001", "S002"])
    assert ranking[0][0] == "S001"
    assert ranking[1][0] == "S002"

def test_generate_transcript():
    setup_mock_data()
    transcript = generate_transcript("S001")
    assert transcript["Student ID"] == "S001"
    assert transcript["Final Grade"] == "B+"
    assert "GPA" in transcript
    assert "Weighted Scores" in transcript

def test_subject_grades():
    setup_mock_data()
    grades_result = subject_grades("S001")
    assert grades_result["Math"] == "A"
    assert grades_result["Physics"] == "B+"
