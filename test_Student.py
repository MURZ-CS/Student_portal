
# Import your functions & global DB
from student_management import (
    students_db,
    validate_student_id,
    add_student,
    generate_roll_number,
    view_students,
    search_student,
    search_by_class,
    update_student,
    delete_student,
    export_students
)

# -----------------------------------------------------------
# FIXTURE — Reset the global dictionary before each test
# -----------------------------------------------------------
@pytest.fixture(autouse=True)
def reset_db():
    students_db.clear()


# -----------------------------------------------------------
# TEST: Student ID validation
# -----------------------------------------------------------
def test_validate_student_id_valid():
    assert validate_student_id("S001") is True
    assert validate_student_id("S450") is True


def test_validate_student_id_invalid():
    assert validate_student_id("A001") is False
    assert validate_student_id("S00X") is False
    assert validate_student_id("001") is False


# -----------------------------------------------------------
# TEST: Adding Students
# -----------------------------------------------------------
def test_add_student_success():
    msg = add_student("S001", "Ali", "10A")
    assert msg == "Student Ali added successfully!"
    assert "S001" in students_db
    assert students_db["S001"]["name"] == "Ali"


def test_add_student_duplicate_id():
    add_student("S001", "Ali", "10A")
    msg = add_student("S001", "Bilal", "10A")
    assert msg == "Error: Student ID already exists."


def test_add_student_invalid_id():
    msg = add_student("X001", "Ali", "10A")
    assert msg == "Error: Invalid student ID format. Use S001, S002 etc."


# -----------------------------------------------------------
# TEST: Roll number generation
# -----------------------------------------------------------
def test_generate_roll_number():
    add_student("S001", "Ali", "10A")
    add_student("S002", "Bilal", "10A")
    roll = generate_roll_number("10A")
    assert roll == 3  # two already exist, next should be 3


# -----------------------------------------------------------
# TEST: View students
# -----------------------------------------------------------
def test_view_students():
    add_student("S001", "Ali", "10A")
    data = view_students()
    assert "S001" in data
    assert data["S001"]["name"] == "Ali"


# -----------------------------------------------------------
# TEST: Search student by ID
# -----------------------------------------------------------
def test_search_student_found():
    add_student("S001", "Ali", "10A")
    result = search_student("S001")
    assert result["name"] == "Ali"


def test_search_student_not_found():
    result = search_student("S999")
    assert result == "Error: Student not found."


# -----------------------------------------------------------
# TEST: Search by class
# -----------------------------------------------------------
def test_search_by_class_found():
    add_student("S001", "Ali", "10A")
    add_student("S002", "Bilal", "10A")
    result = search_by_class("10A")

    assert len(result) == 2
    assert "S001" in result
    assert "S002" in result


def test_search_by_class_not_found():
    result = search_by_class("99Z")
    assert result == "No students found in class 99Z"


# -----------------------------------------------------------
# TEST: Update student
# -----------------------------------------------------------
def test_update_student_success():
    add_student("S001", "Ali", "10A")
    msg = update_student("S001", name="Updated", phone="12345")
    
    assert msg == "Student information updated successfully."
    assert students_db["S001"]["name"] == "Updated"
    assert students_db["S001"]["phone"] == "12345"


def test_update_student_change_class_and_roll():
    add_student("S001", "Ali", "10A")
    add_student("S002", "Bilal", "10A")
    
    msg = update_student("S001", class_name="11B")

    assert msg == "Student information updated successfully."
    assert students_db["S001"]["class"] == "11B"
    assert students_db["S001"]["roll_no"] == 1  # first student in 11B


def test_update_student_not_found():
    msg = update_student("S999", name="Test")
    assert msg == "Error: Student not found."


# -----------------------------------------------------------
# TEST: Deleting student
# -----------------------------------------------------------
def test_delete_student_success():
    add_student("S001", "Ali", "10A")
    msg = delete_student("S001")
    
    assert msg == "Student deleted successfully."
    assert "S001" not in students_db


def test_delete_student_not_found():
    msg = delete_student("S999")
    assert msg == "Error: Student not found."


# -----------------------------------------------------------
# TEST: Exporting students
# -----------------------------------------------------------
def test_export_students(tmp_path):
    # Create temporary file
    filename = tmp_path / "students_test.txt"

    add_student("S001", "Ali", "10A")
    msg = export_students(str(filename))

    assert msg == f"Students exported to {filename}"

    # Verify file content
    with open(filename, "r") as f:
        content = f.read()

    assert "S001" in content
    assert "Ali" in content
