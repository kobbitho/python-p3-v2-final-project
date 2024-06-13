import sqlite3
from .models import Student,Course
def create_tables():
    connection = sqlite3.connect("academics.db")
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS courses(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   course_name TEXT NOT NULL,
                   course_code TEXT NOT NULL,
                   course_description TEXT NOT NULL
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS students(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   first_name TEXT NOT NULL,
                   last_name TEXT NOT NULL,
                   email TEXT NOT NULL,
                   course_id INTEGER,
                   FOREIGN KEY(course_id) REFERENCES courses(id)
    )""")

    connection.commit()
    connection.close()
    print("Tables created successfully.")
create_tables()

class AcademicsDB:
    def __init__(self):
        self.connection = sqlite3.connect("academics.db")
        self.cursor = self.connection.cursor()

    def add_course(self, course_name, course_code, course_description):
        self.cursor.execute("INSERT INTO courses(course_name, course_code, course_description) VALUES (?,?,?)",
                            (course_name, course_code, course_description))
        self.connection.commit()
        print("Course added successfully.")
    def add_student(self, first_name,last_name, email):
        self.cursor.execute("INSERT INTO students(first_name, last_name, email) VALUES (?,?,?)",
                            (first_name, last_name, email))
        self.connection.commit()
        print("Student added successfully.")
    def get_course_by_id(self, course_id):
        self.cursor.execute("SELECT * FROM courses WHERE id =?", (course_id,))
        return self.cursor.fetchone()
    def get_student_by_id(self, student_id):
        self.cursor.execute("SELECT * FROM students WHERE id =?", (student_id,))
        return self.cursor.fetchone()
    def course_exists(self, course_id):
        self.cursor.execute("SELECT * FROM courses WHERE id = ?",(course_id,))
        return self.cursor.fetchone() is not None
    def assign_course_to_student(self, student_id, course_id):
        if self.course_exists(course_id):
            self.cursor.execute("UPDATE students SET course_id = ? WHERE id = ?",
                                (course_id, student_id))
            self.connection.commit()
            print(f'Course{course_id} assigned to student{student_id}')
        else:
            print(f'Course with ID {course_id} does not exist')
    def get_all_courses(self):
        self.cursor.execute("SELECT * FROM courses")
        return self.cursor.fetchall()
    def get_all_students(self):
        query ='''
            SELECT students.id, students.first_name, students.last_name, students.email, courses.id,
            courses.course_name, courses.course_code
            FROM students
            LEFT JOIN courses
            ON students.course_id = courses.id
        '''
        self.cursor.execute(query)
        return self.cursor.fetchall()
    def delete_course(self, course_id):
        self.cursor.execute("DELETE FROM courses WHERE id = ?", (course_id))
        self.connection.commit()
        print(f'Course with ID {course_id} deleted')

    def delete_student(self, student_id):
            self.cursor.execute("DELETE FROM students WHERE id = ?", (student_id))
            self.connection.commit()
            print(f'Student with ID {student_id} deleted')
    def update_course_code(self, course_code, course_id):
        self.cursor.execute("UPDATE courses SET course_code =? WHERE id =?",
                            (course_code, course_id))
        self.connection.commit()
        print(f'Course with ID {course_id} updated')
    def update_student_email(self, email, student_id):
        self.cursor.execute("UPDATE students SET email =? WHERE id =?",
                            (email, student_id))
        self.connection.commit()
        print(f'Student with ID {student_id} updated')

def close(self):
    self.connection.close()

def main():
    db = AcademicsDB()

    while True:
        print("\n1. Add Course")
        print("2. Add Student")
        print("3. Get Course by Id")
        print("4. Get Student by Id")
        print("5. Course Exists")
        print("6. Assign Course to Student")
        print("7. Get All Courses")
        print("8. Get All Students")
        print("9. Delete Course")
        print("10. Delete Student")
        print("11. Update Course Code")
        print("12. Update Student Email")
        print("13. Exit")
        choice = input("Enter choice: ")
      
        if not choice.isdigit():
            print("Invalid choice, please enter a number.")
            continue

        choice = int(choice)

        if choice == 1:
            course_name = input("Enter course name: ")
            course_code = input("Enter course code: ")
            course_description = input("Enter course description: ")
            db.add_course(course_name, course_code, course_description)
        elif choice == 2:
            first_name = input("Enter Student's first name: ")
            last_name = input("Enter Student's last name: ")
            email = input("Enter Student's email: ")
            db.add_student(first_name, last_name, email)
        elif choice == 3:
            course_id = input("Enter course ID: ")
            if not course_id.isdigit():
                print("Invalid course ID, please enter a number.")
                continue
            course_id = int(course_id)
            course = db.get_course_by_id(course_id)
            if course is None:
                print(f"Course with ID {course_id} does not exist")
            else:
                print(f"course ID: {course[0]}, course name: {course[1]}, course code: {course[2]}, course description: {course[3]}")
        elif choice == 4:
            student_id = input("Enter student ID: ")
            if not student_id.isdigit():
                print("Invalid student ID, please enter a number.")
                continue
            student_id = int(student_id)
            student = db.get_student_by_id(student_id)
            if student is None:
                print(f"Student with ID {student_id} does not exist")
            else:
                print(f"student ID: {student[0]}, first name: {student[1]}, last name: {student[2]}, email: {student[3]}, course ID: {student[4]}")
        elif choice == 5:
            course_id = input("Enter course ID: ")
            if not course_id.isdigit():
                print("Invalid course ID, please enter a number.")
                continue
            course_id = int(course_id)
            if db.course_exists(course_id):
                print(f"Course with ID {course_id} exists")
            else:
                print(f"Course with ID {course_id} does not exist")
        elif choice == 6:
            student_id = input("Enter student ID: ")
            if not student_id.isdigit():
                print("Invalid student ID, please enter a number.")
                continue
            student_id = int(student_id)
            course_id = input("Enter course ID: ")
            if not course_id.isdigit():
                print("Invalid course ID, please enter a number.")
                continue
            course_id = int(course_id)
            db.assign_course_to_student(student_id, course_id)
        elif choice == 7:
            courses = db.get_all_courses()
            for course in courses:
                print(f"course ID: {course[0]}, course name: {course[1]}, course code: {course[2]}, course description: {course[3]}")
        elif choice == 8:
            students = db.get_all_students()
            for student in students:
                if student[4] is not None:
                   print(f"student ID: {student[0]}, first name: {student[1]}, last name: {student[2]}, email: {student[3]}, course ID: {student[4]}, course name: {student[5]}, course code: {student[6]}")
                else:
                    print(f"student ID: {student[0]}, first name: {student[1]}, last name: {student[2]}, email: {student[3]}, course: None")
        elif choice == 9:
            course_id = input("Enter course ID: ")
            if not course_id.isdigit():
                print("Invalid course ID, please enter a number.")
                continue
            course_id = int(course_id)
            db.delete_course(course_id)
            print(f'Course with ID {course_id} deleted')
        elif choice == 10:
            student_id = input("Enter student ID: ")
            if not student_id.isdigit():
                print("Invalid student ID, please enter a number.")
                continue
            student_id = int(student_id)
            db.delete_student(student_id)
            print(f'Student with ID {student_id} deleted')
        elif choice == 11:
            course_id = input("Enter course ID: ")
            if not course_id.isdigit():
                print("Invalid course ID, please enter a number.")
                continue
            course_id = int(course_id)
            course_code = input("Enter course code: ")
            db.update_course_code(course_code, course_id)
        elif choice == 12:
            student_id = input("Enter student ID: ")
            if not student_id.isdigit():
                print("Invalid student ID, please enter a number.")
                continue
            student_id = int(student_id)
            email = input("Enter student email: ")
            db.update_student_email(email, student_id)
        elif choice == 13:
            db.close()
            break
        else:
            print("Invalid choice, please try again.")
               
        

if __name__ == "__main__":
    main()




    