# test_marks_validation.py
import pytest
from marks import add_marks, marks

def test_add_marks_boundaries():
    # Clear marks before testing
    marks.clear()

    # Below minimum
    assert add_marks("S1", "Math", "midterm", -5) == "Below minimum (invalid)"

    # Minimum boundary
    assert add_marks("S1", "Math", "midterm", 0) == "Success"

    # Just above minimum
    assert add_marks("S1", "Math", "final", 1) == "Success"

    # Just below maximum
    assert add_marks("S1", "Math", "quiz", 99) == "Success"

    # Maximum boundary
    assert add_marks("S1", "Math", "assignment", 100) == "Success"

    # Above maximum
    assert add_marks("S1", "Math", "project", 101) == "Above maximum (invalid)"

    # Check that valid marks are actually stored
    assert marks["S1"]["Math"]["midterm"] == 0
    assert marks["S1"]["Math"]["final"] == 1
    assert marks["S1"]["Math"]["quiz"] == 99
    assert marks["S1"]["Math"]["assignment"] == 100
