import pytest
from marks import add_marks, view_marks, calculate_percentage, marks

@pytest.fixture(autouse=True)
def reset_marks():
    marks.clear()
    yield

def test_add_and_view_marks():
    assert add_marks("S1", "Math", "midterm", 80) == "Marks added for S1: Math - midterm = 80"
    assert add_marks("S1", "Math", "final", 90) == "Marks added for S1: Math - final = 90"
    
    student_marks = view_marks("S1")
    assert "Math" in student_marks
    assert student_marks["Math"]["midterm"] == 80
    assert student_marks["Math"]["final"] == 90

def test_percentage_calculation():
    add_marks("S1", "Math", "midterm", 80)
    add_marks("S1", "Math", "final", 90)
    percentage = calculate_percentage("S1")
    assert percentage == 85.0
