from Student import (
    add_student, view_students, update_student, delete_student,
    search_student, search_by_class, export_students
)

from teachers import (
    add_teacher, view_teachers, update_teacher, delete_teacher,
    search_by_name, search_by_subject, search_by_class, search_by_id,
    register_teacher, login_teacher, change_teacher_password,
    assign_class, unassign_class, view_assigned_classes,
    add_subject, remove_subject,
    add_teacher_rating, get_average_rating,
    count_teachers
)
from Attandance import (
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


from marks import (
    add_marks,
    view_marks,
    update_marks,
    delete_marks,
    view_subject_marks,
    calculate_percentage,
    best_subject,
    weakest_subject,
    topper,
    class_average,
    generate_full_report
)


from grades import (
    calculate_grade,
    calculate_gpa,
    calculate_cgpa,
    classify_result,
    calculate_weighted_marks,
    rank_students,
    generate_transcript,
    subject_grades
)



# ------------------------------------------------------------
# STUDENT MENU
# ------------------------------------------------------------

def student_menu():
    while True:
        print("\n=== STUDENT MANAGEMENT MENU ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student by ID")
        print("6. Search Students by Class")
        print("7. Export Students")
        print("0. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            sid = input("Student ID (e.g., S001): ")
            name = input("Name: ")
            cls = input("Class: ")
            phone = input("Phone (optional): ")
            address = input("Address (optional): ")
            print(add_student(sid, name, cls, phone, address))

        elif choice == "2":
            print(view_students())

        elif choice == "3":
            sid = input("Student ID to update: ")
            name = input("New Name (leave blank to skip): ")
            cls = input("New Class (leave blank to skip): ")
            phone = input("New Phone (leave blank to skip): ")
            address = input("New Address (leave blank to skip): ")

            # Pass None if blank
            name = name if name.strip() else None
            cls = cls if cls.strip() else None
            phone = phone if phone.strip() else None
            address = address if address.strip() else None

            print(update_student(sid, name, cls, phone, address))

        elif choice == "4":
            sid = input("Student ID to delete: ")
            print(delete_student(sid))

        elif choice == "5":
            sid = input("Enter Student ID: ")
            print(search_student(sid))

        elif choice == "6":
            cls = input("Enter Class: ")
            print(search_by_class(cls))

        elif choice == "7":
            filename = input("Enter filename (e.g., students.txt): ")
            print(export_students(filename))

        elif choice == "0":
            break


# ------------------------------------------------------------
# TEACHER MENU (unchanged)
# ------------------------------------------------------------

def teacher_menu():
    while True:
        print("\n=== TEACHER MANAGEMENT MENU ===")
        print("1. Add Teacher")
        print("2. View Teachers")
        print("3. Update Teacher")
        print("4. Delete Teacher")
        print("5. Search Teacher")
        print("6. Assign Class")
        print("7. Unassign Class")
        print("8. Teachers by Subject")
        print("9. Count Teachers")
        print("0. Back to Main Menu")

        choice = input("Enter choice: ")

        # 1. ADD TEACHER
        if choice == "1":
            tid = input("Teacher ID: ")
            name = input("Name: ")
            subjects = input("Subjects (comma separated): ").split(",")
            classes = input("Classes (comma separated): ").split(",")
            print(add_teacher(tid, name, subjects, classes))

        # 2. VIEW ALL
        elif choice == "2":
            print(view_teachers())

        # 3. UPDATE
        elif choice == "3":
            tid = input("Teacher ID: ")
            name = input("New Name (blank = no change): ") or None
            subjects = input("New Subjects (comma separated) blank = no change: ")
            classes = input("New Classes (comma separated) blank = no change: ")

            subjects = subjects.split(",") if subjects else None
            classes = classes.split(",") if classes else None

            print(update_teacher(tid, name, subjects, classes))

        # 4. DELETE
        elif choice == "4":
            tid = input("Teacher ID to delete: ")
            print(delete_teacher(tid))

        # 5. SEARCH
        elif choice == "5":
            print("\nSearch Options:")
            print("1. By Name")
            print("2. By Subject")
            print("3. By Class")
            print("4. By ID")

            opt = input("Choose: ")

            if opt == "1":
                name = input("Name: ")
                print(search_by_name(name))

            elif opt == "2":
                sub = input("Subject: ")
                print(search_by_subject(sub))

            elif opt == "3":
                cl = input("Class: ")
                print(search_by_class(cl))

            elif opt == "4":
                tid = input("Teacher ID: ")
                print(search_by_id(tid))

        # 6. ASSIGN CLASS
        elif choice == "6":
            tid = input("Teacher ID: ")
            c = input("Class Name: ")
            print(assign_class(tid, c))

        # 7. UNASSIGN CLASS
        elif choice == "7":
            tid = input("Teacher ID: ")
            c = input("Class Name: ")
            print(unassign_class(tid, c))

        # 8. TEACHERS BY SUBJECT
        elif choice == "8":
            sub = input("Subject: ")
            print(search_by_subject(sub))

        # 9. COUNT TEACHERS
        elif choice == "9":
            print("Total Teachers:", count_teachers())

        # EXIT
        elif choice == "0":
            break

        else:
            print("Invalid option!")


# ------------------------------------------------------------
# ATTENDANCE MENU
# ------------------------------------------------------------

def attendance_menu():
    while True:
        print("\n=== ATTENDANCE MANAGEMENT MENU ===")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Update Attendance")
        print("4. Delete Attendance")
        print("5. Bulk Attendance")
        print("6. Monthly Attendance")
        print("7. Attendance Reports")
        print("8. Attendance Analytics")
        print("0. Back to Main Menu")

        choice = input("Enter choice: ")

        # 1. MARK ATTENDANCE
        if choice == "1":
            sid = input("Student ID: ")
            date = input("Date (YYYY-MM-DD): ")
            status = input("Status (P/A/L/LEAVE): ")
            print(mark_attendance(sid, date, status))

        # 2. VIEW ATTENDANCE (full or by student)
        elif choice == "2":
            print("1. View Single Student")
            print("2. View All")
            opt = input("Choose: ")

            if opt == "1":
                sid = input("Student ID: ")
                print(view_attendance(sid))
            else:
                print(view_attendance())

        # 3. UPDATE ATTENDANCE
        elif choice == "3":
            sid = input("Student ID: ")
            date = input("Date (YYYY-MM-DD): ")
            status = input("New Status (P/A/L/LEAVE): ")
            print(update_attendance(sid, date, status))

        # 4. DELETE ATTENDANCE
        elif choice == "4":
            sid = input("Student ID: ")
            date = input("Date (YYYY-MM-DD): ")
            print(delete_attendance(sid, date))

        # 5. BULK ATTENDANCE
        elif choice == "5":
            print("Enter for example: S1:P, S2:A, S3:L")
            date = input("Date (YYYY-MM-DD): ")
            raw = input("Enter data: ")

            # Convert "S1:P, S2:A" → { "S1":"P", "S2":"A" }
            student_status_dict = {}
            for item in raw.split(","):
                sid, st = item.strip().split(":")
                student_status_dict[sid] = st.upper()

            print(mark_bulk_attendance(date, student_status_dict))

        # 6. MONTHLY ATTENDANCE
        elif choice == "6":
            sid = input("Student ID: ")
            month = input("Month (YYYY-MM): ")

            print("Enter statuses for full month separated by space")
            print("Example: P A L P LEAVE A P ...")
            statuses = input("Statuses: ").split()

            print(mark_monthly_attendance(sid, month, statuses))

        # 7. ATTENDANCE REPORTS
        elif choice == "7":
            print("\nAttendance Reports:")
            print("1. Attendance by Date")
            print("2. Attendance by Month")
            print("3. Full Report")

            opt = input("Choose: ")

            if opt == "1":
                date = input("Date (YYYY-MM-DD): ")
                print(view_attendance_by_date(date))

            elif opt == "2":
                sid = input("Student ID: ")
                month = input("Month (YYYY-MM): ")
                print(view_attendance_by_month(sid, month))

            elif opt == "3":
                sid = input("Student ID: ")
                print(get_full_report(sid))

        # 8. ANALYTICS
        elif choice == "8":
            print("\nAttendance Analytics:")
            print("1. Attendance %")
            print("2. Stats Summary")
            print("3. Class Average Attendance")
            print("4. Low Attendance Students (<75%)")
            print("5. Perfect Attendance Students")
            print("6. Best Attendance Days")
            print("7. Worst Attendance Days")

            opt = input("Choose: ")

            if opt == "1":
                sid = input("Student ID: ")
                print("Percentage:", get_attendance_percentage(sid))

            elif opt == "2":
                sid = input("Student ID: ")
                print(get_stats(sid))

            elif opt == "3":
                print("Enter student IDs separated by comma")
                ids = input("IDs: ").split(",")
                ids = [i.strip() for i in ids]
                print("Class Avg:", class_average_attendance(ids))

            elif opt == "4":
                print("Low attendance students:", low_attendance_students())

            elif opt == "5":
                print("Perfect attendance students:", perfect_attendance_students())

            elif opt == "6":
                sid = input("Student ID: ")
                print(best_attendance_days(sid))

            elif opt == "7":
                sid = input("Student ID: ")
                print(worst_attendance_days(sid))

        # EXIT
        elif choice == "0":
            break

        else:
            print("Invalid option!")

# ------------------------------------------------------------
# MARKS MENU
# ------------------------------------------------------------

def marks_menu():
    while True:
        print("\n=== MARKS MANAGEMENT MENU ===")
        print("1. Add Marks")
        print("2. View Marks")
        print("3. Update Marks")
        print("4. Delete Marks")
        print("5. Subject Report")
        print("6. Calculate Percentage")
        print("7. Best & Weakest Subject")
        print("8. Topper / Class Average")
        print("9. Full Report")
        print("0. Back to Main Menu")

        choice = input("Enter choice: ")

        # 1. ADD MARKS
        if choice == "1":
            sid = input("Student ID: ")
            subject = input("Subject: ")
            exam = input("Exam Type (midterm/final/quiz/assignment/project): ")
            score = int(input("Marks (0-100): "))
            print(add_marks(sid, subject, exam, score))

        # 2. VIEW MARKS
        elif choice == "2":
            print("1. View Single Student")
            print("2. View All")
            opt = input("Choose: ")

            if opt == "1":
                sid = input("Student ID: ")
                print(view_marks(sid))
            else:
                print(view_marks())

        # 3. UPDATE MARKS
        elif choice == "3":
            sid = input("Student ID: ")
            subject = input("Subject: ")
            exam = input("Exam Type: ")
            new_score = int(input("New Marks: "))
            print(update_marks(sid, subject, exam, new_score))

        # 4. DELETE MARKS
        elif choice == "4":
            sid = input("Student ID: ")
            subject = input("Subject: ")
            exam = input("Exam Type (leave blank to delete whole subject): ") or None
            print(delete_marks(sid, subject, exam))

        # 5. SUBJECT REPORT
        elif choice == "5":
            sid = input("Student ID: ")
            subject = input("Subject: ")
            print(view_subject_marks(sid, subject))

        # 6. CALCULATE PERCENTAGE
        elif choice == "6":
            sid = input("Student ID: ")
            print("Percentage:", calculate_percentage(sid))

        # 7. BEST & WEAKEST SUBJECT
        elif choice == "7":
            sid = input("Student ID: ")
            print("Best Subject:", best_subject(sid))
            print("Weakest Subject:", weakest_subject(sid))

        # 8. TOPPER / CLASS AVERAGE
        elif choice == "8":
            print("Enter student IDs separated by comma")
            sids = input("IDs: ").split(",")
            sids = [i.strip() for i in sids]
            top, perc = topper(sids)
            print(f"Topper: {top} with {perc:.2f}%")
            print("Class Average:", class_average(sids))

        # 9. FULL REPORT
        elif choice == "9":
            sid = input("Student ID: ")
            print(generate_full_report(sid))

        # EXIT
        elif choice == "0":
            break

        else:
            print("Invalid option!")

# ------------------------------------------------------------
# GRADES MENU
# ------------------------------------------------------------

def grades_menu():
    while True:
        print("\n=== GRADES MENU ===")
        print("1. Calculate Grade (Letter)")
        print("2. Calculate GPA")
        print("3. Calculate CGPA")
        print("4. Result Classification")
        print("5. Weighted Marks")
        print("6. Rank Students")
        print("7. Generate Transcript")
        print("8. Subject-wise Grades")
        print("0. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            sid = input("Student ID: ")
            perc = float(input("Percentage: "))
            print("Letter Grade:", calculate_grade(perc))

        elif choice == "2":
            sid = input("Student ID: ")
            print("GPA:", calculate_gpa(sid))

        elif choice == "3":
            print("Enter GPAs separated by comma")
            gpa_list = [float(g) for g in input("GPAs: ").split(",")]
            print("CGPA:", calculate_cgpa(gpa_list))

        elif choice == "4":
            perc = float(input("Percentage: "))
            print("Result Classification:", classify_result(perc))

        elif choice == "5":
            sid = input("Student ID: ")
            print("Weighted Marks:", calculate_weighted_marks(sid))

        elif choice == "6":
            print("Enter student IDs separated by comma")
            sids = [i.strip() for i in input("IDs: ").split(",")]
            ranking = rank_students(sids)
            print("Ranking (Student ID, Percentage):", ranking)

        elif choice == "7":
            sid = input("Student ID: ")
            print("Transcript:", generate_transcript(sid))

        elif choice == "8":
            sid = input("Student ID: ")
            print("Subject-wise Grades:", subject_grades(sid))

        elif choice == "0":
            break

        else:
            print("Invalid option!")


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
