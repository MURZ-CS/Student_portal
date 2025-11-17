import pytest
from teachers import (
    teachers,
    add_teacher,
    view_teachers,
    update_teacher,
    delete_teacher,
    search_by_name,
    search_by_subject,
    search_by_class,
    search_by_id,
    assign_class,
    unassign_class,
    add_subject,
    remove_subject,
    add_teacher_rating,
    get_average_rating,
    count_teachers
)

@pytest.fixture(autouse=True)
def reset_data():
    teachers.clear()
    yield


def test_add_teacher():
    result = add_teacher("T001", "Mr. John")
    assert "added successfully" in result
    assert "T001" in teachers

def test_update_teacher():
    add_teacher("T002", "Ms. Rose")
    result = update_teacher("T002", name="Ms. Rosa", subject=["Math"], assigned_class=["10A"])
    assert result == "Teacher details updated."
    assert teachers["T002"]["name"] == "Ms. Rosa"
    assert "Math" in teachers["T002"]["subject"]
    assert "10A" in teachers["T002"]["class"]

def test_delete_teacher():
    add_teacher("T003", "Mr. Khan")
    result = delete_teacher("T003")
    assert "deleted successfully" in result
    assert "T003" not in teachers

def test_search_by_name_subject_class_id():
    add_teacher("T004", "Mrs. Lee", subject=["Science"], assigned_class=["10A"])
    assert "T004" in search_by_name("Mrs. Lee")
    assert "T004" in search_by_subject("Science")
    assert "T004" in search_by_class("10A")
    assert search_by_id("T004")["name"] == "Mrs. Lee"

def test_assign_unassign_class():
    add_teacher("T005", "Ms. Kim")
    assign_class("T005", "9B")
    assert "9B" in teachers["T005"]["class"]
    unassign_class("T005", "9B")
    assert "9B" not in teachers["T005"]["class"]

def test_add_remove_subject():
    add_teacher("T006", "Mr. Lee")
    add_subject("T006", "English")
    assert "English" in teachers["T006"]["subject"]
    remove_subject("T006", "English")
    assert "English" not in teachers["T006"]["subject"]

def test_teacher_rating():
    add_teacher("T007", "Ms. Park")
    add_teacher_rating("T007", 4)
    add_teacher_rating("T007", 5)
    avg = get_average_rating("T007")
    assert avg == 4.5

def test_count_teachers():
    add_teacher("T008", "Mr. White")
    add_teacher("T009", "Ms. Black")
    assert count_teachers() == 2
