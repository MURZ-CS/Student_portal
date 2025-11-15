

marks = {}
VALID_EXAMS = ["midterm", "final", "quiz", "assignment", "project"]



marks = {}
VALID_EXAMS = ["midterm", "final", "quiz", "assignment", "project"]

def add_marks(student_id, subject, exam_type, score):
    """Add marks for a student in a specific subject and exam (no validation)."""
    exam_type = exam_type.lower()

    if student_id not in marks:
        marks[student_id] = {}

    if subject not in marks[student_id]:
        marks[student_id][subject] = {}

    marks[student_id][subject][exam_type] = score

    return "Success"

def view_marks(student_id=None):
    """View marks of all students or a single student."""
    if student_id:
        return marks.get(student_id, "No marks found for this student.")
    return marks




def update_marks(student_id, subject, exam_type, new_score):
    if student_id not in marks:
        return "Student not found."

    if subject not in marks[student_id]:
        return "Subject not found."

    if exam_type not in marks[student_id][subject]:
        return "Exam record not found."

    if not (0 <= new_score <= 100):
        return "Invalid marks (0-100)."

    marks[student_id][subject][exam_type] = new_score
    return "Marks updated successfully."


def delete_marks(student_id, subject, exam_type=None):
    """Delete a specific exam record or the whole subject."""
    if student_id not in marks:
        return "Student not found."

    if subject not in marks[student_id]:
        return "Subject not found."

    if exam_type:
        if exam_type not in marks[student_id][subject]:
            return "Exam not found."

        del marks[student_id][subject][exam_type]
        return f"{exam_type} deleted."

    else:
        del marks[student_id][subject]
        return "Subject deleted."



# ---------------------------- SUBJECT REPORTS -------------------------------

def view_subject_marks(student_id, subject):
    if student_id not in marks:
        return "Student not found."
    return marks[student_id].get(subject, "Subject not found.")



# ---------------------------- TOTALS & PERCENTAGES -------------------------

def calculate_total_marks(student_id):
    """Calculate total marks across all subjects and exams."""
    if student_id not in marks:
        return 0

    total = 0
    for subject in marks[student_id]:
        total += sum(marks[student_id][subject].values())
    return total


def calculate_percentage(student_id):
    """Calculate percentage assuming each exam is out of 100."""
    if student_id not in marks:
        return 0

    total_exams = sum(len(marks[student_id][subject]) for subject in marks[student_id])
    if total_exams == 0:
        return 0

    total_marks = calculate_total_marks(student_id)
    return (total_marks / (total_exams * 100)) * 100



# ---------------------------- ANALYTICS -------------------------------------

def best_subject(student_id):
    """Return subject with highest average score."""
    if student_id not in marks:
        return "Student not found."

    best = None
    best_avg = -1

    for subject, exams in marks[student_id].items():
        avg = sum(exams.values()) / len(exams)
        if avg > best_avg:
            best_avg = avg
            best = subject

    return best, best_avg


def weakest_subject(student_id):
    """Return subject with lowest average score."""
    if student_id not in marks:
        return "Student not found."

    weak = None
    lowest_avg = 999

    for subject, exams in marks[student_id].items():
        avg = sum(exams.values()) / len(exams)
        if avg < lowest_avg:
            lowest_avg = avg
            weak = subject

    return weak, lowest_avg


def topper(students):
    """Return the student with highest overall percentage."""
    top_student = None
    highest_perc = -1

    for sid in students:
        p = calculate_percentage(sid)
        if p > highest_perc:
            highest_perc = p
            top_student = sid

    return top_student, highest_perc


def class_average(students):
    """Calculate the class average percentage."""
    if not students:
        return 0

    total = sum(calculate_percentage(sid) for sid in students)
    return total / len(students)



# ---------------------------- GRADE ANALYSIS ------------------------------

def grade_from_score(score):
    """Convert numeric score to grade."""
    if score >= 90: return "A+"
    if score >= 80: return "A"
    if score >= 70: return "B+"
    if score >= 60: return "B"
    if score >= 50: return "C"
    if score >= 40: return "D"
    return "F"


def subject_wise_grade(student_id):
    """Return grade subject-wise (average marks per subject)."""
    if student_id not in marks:
        return "Student not found."

    result = {}
    for subject, exams in marks[student_id].items():
        avg = sum(exams.values()) / len(exams)
        result[subject] = grade_from_score(avg)

    return result



# ---------------------------- FULL DETAILED REPORT --------------------------

def generate_full_report(student_id):
    """Return complete marks report with analytics."""
    if student_id not in marks:
        return "Student not found."

    report = {
        "Marks": marks[student_id],
        "Total Marks": calculate_total_marks(student_id),
        "Percentage": calculate_percentage(student_id),
        "Best Subject": best_subject(student_id),
        "Weakest Subject": weakest_subject(student_id),
        "Grades": subject_wise_grade(student_id)
    }

    return report
