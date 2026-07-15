import json


class Task:
    def __init__(self, task_id, title, completed=False):
        self.task_id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.task_id,
            "title": self.title,
            "completed": self.completed
        }


class TodoManager:

    def __init__(self):
        self.tasks = []
        self.load_tasks()


    def add_task(self):
        task_id = input("Enter task ID: ")
        title = input("Enter task: ")

        task = Task(task_id, title)
        self.tasks.append(task)

        self.save_tasks()
        print("Task added successfully!")


    def view_tasks(self):
        if not self.tasks:
            print("No tasks available")
            return

        for task in self.tasks:
            status = "Completed" if task.completed else "Pending"

            print("----------------")
            print("ID:", task.task_id)
            print("Task:", task.title)
            print("Status:", status)


    def edit_task(self):
        task_id = input("Enter task ID to edit: ")

        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input("Enter new task: ")
                self.save_tasks()
                print("Task updated!")
                return

        print("Task not found")


    def delete_task(self):
        task_id = input("Enter task ID to delete: ")

        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print("Task deleted!")
                return

        print("Task not found")


    def complete_task(self):
        task_id = input("Enter task ID to complete: ")

        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = True
                self.save_tasks()
                print("Task completed!")
                return

        print("Task not found")


    def save_tasks(self):
        data = [task.to_dict() for task in self.tasks]

        with open("tasks.json", "w") as file:
            json.dump(data, file)


    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                data = json.load(file)

                for task in data:
                    self.tasks.append(
                        Task(
                            task["id"],
                            task["title"],
                            task["completed"]
                        )
                    )

        except FileNotFoundError:
            pass



manager = TodoManager()


while True:
    print("""
====== To-Do Manager ======

1. Add Task
2. View Tasks
3. Edit Task
4. Delete Task
5. Mark Completed
6. Exit
""")

    choice = input("Choose option: ")

    if choice == "1":
        manager.add_task()

    elif choice == "2":
        manager.view_tasks()

    elif choice == "3":
        manager.edit_task()

    elif choice == "4":
        manager.delete_task()

    elif choice == "5":
        manager.complete_task()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")