import json


class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def to_dict(self):
        return {
            "id": self.emp_id,
            "name": self.name,
            "position": self.position,
            "salary": self.salary
        }


class EmployeeManager:

    def __init__(self):
        self.employees = []
        self.load_data()


    def add_employee(self):
        emp_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        position = input("Enter position: ")
        salary = input("Enter salary: ")

        employee = Employee(emp_id, name, position, salary)
        self.employees.append(employee)

        self.save_data()
        print("Employee added successfully!")


    def view_employees(self):
        if not self.employees:
            print("No employees found")
            return

        for emp in self.employees:
            print("----------------")
            print("ID:", emp.emp_id)
            print("Name:", emp.name)
            print("Position:", emp.position)
            print("Salary:", emp.salary)


    def search_employee(self):
        emp_id = input("Enter employee ID: ")

        for emp in self.employees:
            if emp.emp_id == emp_id:
                print("Employee found:")
                print("Name:", emp.name)
                print("Position:", emp.position)
                print("Salary:", emp.salary)
                return

        print("Employee not found")


    def update_salary(self):
        emp_id = input("Enter employee ID: ")

        for emp in self.employees:
            if emp.emp_id == emp_id:
                emp.salary = input("Enter new salary: ")

                self.save_data()
                print("Salary updated!")
                return

        print("Employee not found")


    def remove_employee(self):
        emp_id = input("Enter employee ID: ")

        for emp in self.employees:
            if emp.emp_id == emp_id:

                self.employees.remove(emp)
                self.save_data()

                print("Employee removed!")
                return

        print("Employee not found")


    def save_data(self):
        data = [emp.to_dict() for emp in self.employees]

        with open("employees.json", "w") as file:
            json.dump(data, file)


    def load_data(self):
        try:
            with open("employees.json", "r") as file:
                data = json.load(file)

                for emp in data:
                    self.employees.append(
                        Employee(
                            emp["id"],
                            emp["name"],
                            emp["position"],
                            emp["salary"]
                        )
                    )

        except FileNotFoundError:
            pass



manager = EmployeeManager()


while True:

    print("""
===== Employee Management System =====

1. Add Employee
2. View Employees
3. Search Employee
4. Update Salary
5. Remove Employee
6. Exit
""")

    choice = input("Choose option: ")

    if choice == "1":
        manager.add_employee()

    elif choice == "2":
        manager.view_employees()

    elif choice == "3":
        manager.search_employee()

    elif choice == "4":
        manager.update_salary()

    elif choice == "5":
        manager.remove_employee()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")