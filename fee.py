# fees.py

fees_db = {}

def add_student_fee(student_id, amount):
    fees_db.setdefault(student_id, {"total": 0, "paid": 0})
    fees_db[student_id]["total"] += amount
    return f"Added fee {amount} for {student_id}."

def record_payment(student_id, amount):
    if student_id not in fees_db:
        return "Student not found."
    fees_db[student_id]["paid"] += amount
    return f"Payment of {amount} recorded."

def check_balance(student_id):
    if student_id not in fees_db:
        return "Student not found."
    total = fees_db[student_id]["total"]
    paid = fees_db[student_id]["paid"]
    return total - paid

def generate_fee_report(student_id=None):
    if student_id:
        return fees_db.get(student_id, {})
    return fees_db
