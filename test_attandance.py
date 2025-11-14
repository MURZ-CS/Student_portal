import pytest
from Attandance import (
    attendance,
    mark_attendance,
    view_attendance,
    update_attendance,
    delete_attendance,
    mark_bulk_attendance,
    mark_monthly_attendance,
    view_attendance_by_date,
    view_attendance_by_month,
    get_full_report,
    get_attendance_percentage,
    get_stats,
    class_average_attendance,
    low_attendance_students,
    perfect_attendance_students,
    best_attendance_days,
    worst_attendance_days
)

# ----------------- FIXTURE TO RESET DATA ----------------- #
@pytest.fixture(autouse=True)
def reset_data():
    attendance.clear()
    yield


# ==================== SIMPLE TESTS ==================== #

def test_mark_attendance():
    result = mark_attendance("S001", "2025-11-01", "P")
    assert "marked" in result
    assert attendance["S001"]["2025-11-01"] == "P"

def test_mark_invalid_status():
    result = mark_attendance("S002", "2025-11-01", "X")
    assert "Invalid status" in result

def test_view_attendance():
    mark_attendance("S003", "2025-11-01", "A")
    records = view_attendance("S003")
    assert records["2025-11-01"] == "A"

def test_update_attendance():
    mark_attendance("S004", "2025-11-01", "L")
    result = update_attendance("S004", "2025-11-01", "P")
    assert "updated" in result
    assert attendance["S004"]["2025-11-01"] == "P"

def test_delete_attendance():
    mark_attendance("S005", "2025-11-01", "P")
    result = delete_attendance("S005", "2025-11-01")
    assert "deleted" in result
    assert "2025-11-01" not in attendance.get("S005", {})

def test_mark_bulk_attendance():
    students = {"S006": "P", "S007": "A"}
    result = mark_bulk_attendance("2025-11-02", students)
    assert "Bulk" in result
    assert attendance["S006"]["2025-11-02"] == "P"
    assert attendance["S007"]["2025-11-02"] == "A"

def test_mark_monthly_attendance():
    month_status = ["P"] * 30
    result = mark_monthly_attendance("S008", "2025-11", month_status)
    assert "Monthly" in result
    assert len(attendance["S008"]) == 30

def test_view_attendance_by_date():
    mark_attendance("S009", "2025-11-03", "P")
    records = view_attendance_by_date("2025-11-03")
    assert records["S009"] == "P"

def test_view_attendance_by_month():
    month_status = ["A"] * 5
    mark_monthly_attendance("S010", "2025-11", month_status + ["P"]*25)
    records = view_attendance_by_month("S010", "2025-11")
    assert len(records) == 30

def test_get_full_report():
    mark_attendance("S011", "2025-11-01", "P")
    report = get_full_report("S011")
    assert "2025-11-01" in report

def test_get_attendance_percentage():
    mark_attendance("S012", "2025-11-01", "P")
    mark_attendance("S012", "2025-11-02", "A")
    percent = get_attendance_percentage("S012")
    assert percent == 50

def test_get_stats():
    mark_attendance("S013", "2025-11-01", "P")
    mark_attendance("S013", "2025-11-02", "A")
    stats = get_stats("S013")
    assert stats["Present"] == 1
    assert stats["Absent"] == 1

def test_class_average_attendance():
    mark_attendance("S014", "2025-11-01", "P")
    mark_attendance("S015", "2025-11-01", "A")
    avg = class_average_attendance(["S014", "S015"])
    assert avg == 50

def test_low_and_perfect_attendance_students():
    mark_attendance("S016", "2025-11-01", "P")
    mark_attendance("S017", "2025-11-01", "A")
    low = low_attendance_students(75)
    perfect = perfect_attendance_students()
    assert "S017" in low
    assert "S016" in perfect

def test_best_worst_days():
    mark_attendance("S018", "2025-11-01", "P")
    mark_attendance("S018", "2025-11-02", "A")
    best = best_attendance_days("S018")
    worst = worst_attendance_days("S018")
    assert "2025-11-01" in best
    assert "2025-11-02" in worst
