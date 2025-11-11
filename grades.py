# grades.py
def calculate_grade(percentage):
    if percentage >= 95:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B+'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'F'

def calculate_percentage(marks_dict):
    if not marks_dict:
        return 0
    total = sum(marks_dict.values())
    return total / len(marks_dict)
