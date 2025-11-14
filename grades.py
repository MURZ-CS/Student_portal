# grades.py

from marks import calculate_percentage, marks


# ==============================
# GRADE SYSTEM CONFIG
# ==============================

GRADE_BOUNDARIES = {
    "A+": (90, 100),
    "A": (80, 89),
    "B+": (70, 79),
    "B": (60, 69),
    "C": (50, 59),
    "D": (40, 49),
    "F": (0, 39)
}

GRADE_POINTS = {
    "A+": 4.0,
    "A": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0
}

RESULT_CLASSIFICATION = {
    "Distinction": (75, 100),
    "Merit": (60, 74),
    "Pass": (40, 59),
    "Fail": (0, 39)
}

# Default weightage
DEFAULT_WEIGHTAGE = {
    "midterm": 0.4,
    "final": 0.6
}



# ==============================
# LETTER GRADE CALCULATION
# ==============================

def calculate_grade(percentage):
    for grade, (low, high) in GRADE_BOUNDARIES.items():
        if low <= percentage <= high:
            return grade
    return "Invalid Percentage"



# ==============================
# GRADE POINT CALCULATION
# ==============================

def get_grade_point(letter_grade):
    return GRADE_POINTS.get(letter_grade, 0.0)



# ==============================
# GPA CALCULATION (Per Student)
# ==============================

def calculate_gpa(student_id):
    if student_id not in marks:
        return "No marks found."

    total_points = 0
    subject_count = 0

    for subject, exams in marks[student_id].items():
        # Average marks per subject
        avg = sum(exams.values()) / len(exams)

        grade = calculate_grade(avg)
        grade_point = get_grade_point(grade)

        total_points += grade_point
        subject_count += 1

    if subject_count == 0:
        return 0.0

    return round(total_points / subject_count, 2)



# ==============================
# CGPA (SEMESTER-WISE) CALCULATION
# ==============================

def calculate_cgpa(gpa_list):
    if not gpa_list:
        return 0.0
    return round(sum(gpa_list) / len(gpa_list), 2)



# ==============================
# RESULT CLASSIFICATION
# ==============================

def classify_result(percentage):
    for status, (low, high) in RESULT_CLASSIFICATION.items():
        if low <= percentage <= high:
            return status
    return "Unknown"



# ==============================
# WEIGHTED GRADE CALCULATION
# ==============================

def calculate_weighted_marks(student_id):
    if student_id not in marks:
        return "Student not found."

    weighted_results = {}

    for subject, exams in marks[student_id].items():
        total = 0

        for exam, score in exams.items():
            weight = DEFAULT_WEIGHTAGE.get(exam, 0)
            total += score * weight

        weighted_results[subject] = round(total, 2)

    return weighted_results



# ==============================
# RANKING (LIST OF STUDENTS)
# ==============================

def rank_students(student_list):
    ranking = []

    for sid in student_list:
        percentage = calculate_percentage(sid)
        ranking.append((sid, percentage))

    ranking.sort(key=lambda x: x[1], reverse=True)
    return ranking



# ==============================
# TRANSCRIPT GENERATION
# ==============================

def generate_transcript(student_id):
    if student_id not in marks:
        return "Student not found."

    percentage = calculate_percentage(student_id)
    grade = calculate_grade(percentage)
    gpa = calculate_gpa(student_id)
    result_status = classify_result(percentage)
    weighted = calculate_weighted_marks(student_id)

    transcript = {
        "Student ID": student_id,
        "Marks": marks[student_id],
        "Weighted Scores": weighted,
        "Percentage": percentage,
        "Final Grade": grade,
        "GPA": gpa,
        "Result Status": result_status
    }

    return transcript



# ==============================
# SUBJECT GRADE BREAKDOWN
# ==============================

def subject_grades(student_id):
    if student_id not in marks:
        return "Student not found."

    result = {}

    for subject, exams in marks[student_id].items():
        avg = sum(exams.values()) / len(exams)
        letter_grade = calculate_grade(avg)
        result[subject] = letter_grade

    return result
