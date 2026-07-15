import json


class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }


class StudentManager:

    def __init__(self):
        self.students = []
        self.load_data()

    def add_student(self):
        sid = input("Enter student ID: ")
        name = input("Enter name: ")
        age = input("Enter age: ")
        grade = input("Enter grade: ")

        student = Student(sid, name, age, grade)
        self.students.append(student)

        self.save_data()
        print("Student added successfully!")


    def view_students(self):
        if not self.students:
            print("No students found")
            return

        for s in self.students:
            print("----------------")
            print("ID:", s.student_id)
            print("Name:", s.name)
            print("Age:", s.age)
            print("Grade:", s.grade)


    def search_student(self):
        sid = input("Enter student ID to search: ")

        for s in self.students:
            if s.student_id == sid:
                print("Student found:")
                print(s.name, s.age, s.grade)
                return

        print("Student not found")


    def update_student(self):
        sid = input("Enter student ID: ")

        for s in self.students:
            if s.student_id == sid:
                s.name = input("New name: ")
                s.age = input("New age: ")
                s.grade = input("New grade: ")

                self.save_data()
                print("Updated successfully")
                return

        print("Student not found")


    def delete_student(self):
        sid = input("Enter student ID: ")

        for s in self.students:
            if s.student_id == sid:
                self.students.remove(s)
                self.save_data()
                print("Deleted successfully")
                return

        print("Student not found")


    def save_data(self):
        data = [s.to_dict() for s in self.students]

        with open("students.json", "w") as file:
            json.dump(data, file)


    def load_data(self):
        try:
            with open("students.json", "r") as file:
                data = json.load(file)

                for s in data:
                    self.students.append(
                        Student(
                            s["id"],
                            s["name"],
                            s["age"],
                            s["grade"]
                        )
                    )

        except FileNotFoundError:
            pass



manager = StudentManager()


while True:
    print("""
==== Student Management System ====

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
""")

    choice = input("Choose option: ")

    if choice == "1":
        manager.add_student()

    elif choice == "2":
        manager.view_students()

    elif choice == "3":
        manager.search_student()

    elif choice == "4":
        manager.update_student()

    elif choice == "5":
        manager.delete_student()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")