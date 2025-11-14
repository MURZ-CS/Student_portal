from Student import (
    add_student, view_students, update_student, delete_student,
    search_student_by_id, search_student_by_name, promote_student,
    count_students_by_class, export_students_csv, import_students_csv
)

from teachers import (
    add_teacher, view_teachers, update_teacher, delete_teacher,
    search_teacher, assign_subject, unassign_subject,
    list_teachers_by_subject, teacher_count
)

from Attandance import (
    mark_attendance, view_attendance, view_attendance_by_student,
    attendance_percentage, monthly_report, most_regular_students,
    least_regular_students
)

from marks import (
    add_marks, view_marks, update_marks, delete_marks,
    subject_topper, class_average, export_marks_csv
)

from grades import (
    calculate_grade, calculate_percentage, generate_report_card,
    class_wise_grade_distribution, overall_topper, grade_summary
)


# ------------------------------------------------------------
# MASTER MENU
# ------------------------------------------------------------

def student_menu():
    while True:
        print("\n=== STUDENT MANAGEMENT MENU ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search by ID")
        print("6. Search by Name")
        print("7. Promote Student")
        print("8. Count Students by Class")
        print("9. Export Students to CSV")
        print("10. Import Students from CSV")
        print("0. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            sid = input("Student ID: ")
            name = input("Name: ")
            cls = input("Class: ")
            add_student(sid, name, cls)

        elif choice == "2":
            print(view_students())

        elif choice == "3":
            sid = input("Student ID to update: ")
            name = input("New Name: ")
            cls = input("New Class: ")
            update_student(sid, name, cls)

        elif choice == "4":
            sid = input("Student ID to delete: ")
            delete_student(sid)

        elif choice == "5":
            sid = input("Student ID: ")
            print(search_student_by_id(sid))

        elif choice == "6":
            name = input("Name: ")
            print(search_student_by_name(name))

        elif choice == "7":
            sid = input("Student ID: ")
            promote_student(sid)

        elif choice == "8":
            cls = input("Class: ")
            print(count_students_by_class(cls))

        elif choice == "9":
            filename = input("CSV file name: ")
            export_students_csv(filename)

        elif choice == "10":
            filename = input("CSV file name: ")
            import_students_csv(filename)

        elif choice == "0":
            break


def teacher_menu():
    while True:
        print("\n=== TEACHER MANAGEMENT MENU ===")
        print("1. Add Teacher")
        print("2. View Teachers")
        print("3. Update Teacher")
        print("4. Delete Teacher")
        print("5. Search Teacher")
        print("6. Assign Subject")
        print("7. Unassign Subject")
        print("8. Teachers by Subject")
        print("9. Count Teachers")
        print("0. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            tid = input("Teacher ID: ")
            name = input("Name: ")
            subject = input("Subject: ")
            add_teacher(tid, name, subject)

        elif choice == "2":
            print(view_teachers())

        elif choice == "3":
            tid = input("Teacher ID: ")
            name = input("New Name: ")
            subject = input("New Subject: ")
            update_teacher(tid, name, subject)

        elif choice == "4":
            tid = input("Teacher ID to delete: ")
            delete_teacher(tid)

        elif choice == "5":
            tid = input("Teacher ID: ")
            print(search_teacher(tid))

        elif choice == "6":
            tid = input("Teacher ID: ")
            sub = input("Subject: ")
            assign_subject(tid, sub)

        elif choice == "7":
            tid = input("Teacher ID: ")
            sub = input("Subject: ")
            unassign_subject(tid, sub)

        elif choice == "8":
            sub = input("Subject: ")
            print(list_teachers_by_subject(sub))

        elif choice == "9":
            print("Total Teachers:", teacher_count())

        elif choice == "0":
            break


def attendance_menu():
    while True:
        print("\n=== ATTENDANCE MENU ===")
        print("1. Mark Attendance")
        print("2. View All Attendance")
        print("3. View Attendance by Student")
        print("4. Attendance Percentage")
        print("5. Monthly Attendance Report")
        print("6. Most Regular Students")
        print("7. Least Regular Students")
        print("0. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            sid = input("Student ID: ")
            date = input("Date (YYYY-MM-DD): ")
            status = input("Present/Absent: ")
            mark_attendance(sid, date, status)

        elif choice == "2":
            print(view_attendance())

        elif choice == "3":
            sid = input("Student ID: ")
            print(view_attendance_by_student(sid))

        elif choice == "4":
            sid = input("Student ID: ")
            print(attendance_percentage(sid))

        elif choice == "5":
            sid = input("Student ID: ")
            month = input("Month (1–12): ")
            print(monthly_report(sid, month))

        elif choice == "6":
            print(most_regular_students())

        elif choice == "7":
            print(least_regular_students())

        elif choice == "0":
            break


def marks_menu():
    while True:
        print("\n=== MARKS MENU ===")
        print("1. Add Marks")
        print("2. View Marks")
        print("3. Update Marks")
        print("4. Delete Marks")
        print("5. Subject Topper")
        print("6. Class Average")
        print("7. Export Marks CSV")
        print("0. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            sid = input("Student ID: ")
            subject = input("Subject: ")
            marks = int(input("Marks: "))
            add_marks(sid, subject, marks)

        elif choice == "2":
            print(view_marks())

        elif choice == "3":
            sid = input("Student ID: ")
            subject = input("Subject: ")
            marks = int(input("New Marks: "))
            update_marks(sid, subject, marks)

        elif choice == "4":
            sid = input("Student ID: ")
            subject = input("Subject: ")
            delete_marks(sid, subject)

        elif choice == "5":
            subject = input("Subject: ")
            print(subject_topper(subject))

        elif choice == "6":
            subject = input("Subject: ")
            print(class_average(subject))

        elif choice == "7":
            filename = input("File name: ")
            export_marks_csv(filename)

        elif choice == "0":
            break


def grades_menu():
    while True:
        print("\n=== GRADES MENU ===")
        print("1. Calculate Percentage")
        print("2. Calculate Grade")
        print("3. Generate Report Card")
        print("4. Class-wise Grade Distribution")
        print("5. Overall Topper")
        print("6. Grade Summary")
        print("0. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            sid = input("Student ID: ")
            print(calculate_percentage(sid))

        elif choice == "2":
            sid = input("Student ID: ")
            print(calculate_grade(sid))

        elif choice == "3":
            sid = input("Student ID: ")
            print(generate_report_card(sid))

        elif choice == "4":
            cls = input("Class: ")
            print(class_wise_grade_distribution(cls))

        elif choice == "5":
            print(overall_topper())

        elif choice == "6":
            print(grade_summary())

        elif choice == "0":
            break


# ------------------------------------------------------------
# MAIN PROGRAM LOOP
# ------------------------------------------------------------

def main():
    while True:
        print("\n=========== MAIN MENU ===========")
        print("1. Student Management")
        print("2. Teacher Management")
        print("3. Attendance Management")
        print("4. Marks Management")
        print("5. Grades Processing")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            student_menu()
        elif choice == "2":
            teacher_menu()
        elif choice == "3":
            attendance_menu()
        elif choice == "4":
            marks_menu()
        elif choice == "5":
            grades_menu()
        elif choice == "0":
            print("Exiting system...")
            break


if __name__ == "__main__":
    main()
