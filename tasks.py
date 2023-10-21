import pickle

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("1. Add a new task")
        print("2. Display all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Save tasks to a file")
        print("6. Load tasks from a file")
        print("7. Quit")

    def add_task(self):
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        task = Task(title, description)
        self.tasks.append(task)
        print("Task added successfully!")

    def display_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            status = "Completed" if task.completed else "Not Completed"
            print(f"{i}. {task.title} - {task.description} ({status})")

    def mark_completed(self):
        self.display_tasks()
        try:
            index = int(input("Enter the task number to mark as completed: ")) - 1
            self.tasks[index].completed = True
            print("Task marked as completed!")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid task number.")

    def delete_task(self):
        self.display_tasks()
        try:
            index = int(input("Enter the task number to delete: ")) - 1
            del self.tasks[index]
            print("Task deleted successfully!")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid task number.")

    def save_tasks(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.tasks, file)
        print("Tasks saved to file successfully!")

    def load_tasks(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.tasks = pickle.load(file)
            print("Tasks loaded from file successfully!")
        except FileNotFoundError:
            print("File not found. No tasks loaded.")
        except Exception as e:
            print(f"An error occurred while loading tasks: {e}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-7): ")

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.display_tasks()
            elif choice == '3':
                self.mark_completed()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                filename = input("Enter the filename to save tasks: ")
                self.save_tasks(filename)
            elif choice == '6':
                filename = input("Enter the filename to load tasks from: ")
                self.load_tasks(filename)
            elif choice == '7':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    manager = TaskManager()
    manager.run()
