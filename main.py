# main.py
from Student import add_student, view_students
from teachers import add_teacher, view_teachers
from Attandance import mark_attendance, view_attendance
from marks import add_marks, view_marks
from grades import calculate_grade, calculate_percentage

def main():
    while True:
        print("\n--- Student Portal ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Add Teacher")
        print("4. View Teachers")
        print("5. Mark Attendance")
        print("6. View Attendance")
        print("7. Add Marks")
        print("8. View Marks & Grades")
        print("9. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            student_id = input("Student ID: ")
            name = input("Name: ")
            class_name = input("Class: ")
            success, msg = add_student(student_id, name, class_name)
            print(msg)

        elif choice == '2':
            students = view_students()
            for sid, data in students.items():
                print(f"{sid}: {data}")

        elif choice == '3':
            teacher_id = input("Teacher ID: ")
            name = input("Name: ")
            subject = input("Subject: ")
            success, msg = add_teacher(teacher_id, name, subject)
            print(msg)

        elif choice == '4':
            teachers = view_teachers()
            for tid, data in teachers.items():
                print(f"{tid}: {data}")

        elif choice == '5':
            student_id = input("Student ID: ")
            date = input("Date (YYYY-MM-DD): ")
            success, msg = mark_attendance(student_id, date)
            print(msg)

        elif choice == '6':
            student_id = input("Student ID: ")
            attendance = view_attendance(student_id)
            print(f"Attendance for {student_id}: {attendance}")

        elif choice == '7':
            student_id = input("Student ID: ")
            subject = input("Subject: ")
            marks = float(input("Marks: "))
            success, msg = add_marks(student_id, subject, marks)
            print(msg)

        elif choice == '8':
            student_id = input("Student ID: ")
            marks_dict = view_marks(student_id)
            print(f"Marks: {marks_dict}")
            percentage = calculate_percentage(marks_dict)
            grade = calculate_grade(percentage)
            print(f"Percentage: {percentage:.2f}% | Grade: {grade}")

        elif choice == '9':
            print("Exiting portal...")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
