
import json
import os


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load()

    # Load tasks from JSON file
    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.tasks = json.load(f)

    # Save tasks to JSON file
    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=2)

    # Add a new task
    def add_task(self, title):
        title = title.strip()
        if not title:
            raise ValueError("Task title cannot be empty.")
        if len(title) > 100:
            raise ValueError("Task title is too long (max 100 characters).")
        task_id = max([t["id"] for t in self.tasks], default=0) + 1
        task = {"id": task_id, "title": title, "done": False}
        self.tasks.append(task)
        self.save()
        return task

    # Return all tasks
    def list_tasks(self):
        return self.tasks

    # Mark a task as complete
    def complete_task(self, task_id):
        for t in self.tasks:
            if t["id"] == task_id:
                t["done"] = True
                self.save()
                return True

        return False

    # Display all tasks
    def show_tasks(self):
        tasks = self.list_tasks()

        if not tasks:
            print("No tasks yet.")
            return

        for t in tasks:
            status = "[x]" if t["done"] else "[ ]"
            print(f"{t['id']}. {status} {t['title']}")


# Main program
def main():
    manager = TaskManager()

    while True:
        print("\n--- Student Task Manager ---")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Complete task")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                title = input("Task title: ").strip()

                if not title:
                    print("Task title cannot be empty.")
                    continue

                task = manager.add_task(title)
                print(f"Added task #{task['id']}")

            elif choice == "2":
                manager.show_tasks()

            elif choice == "3":
                task_id = int(input("Task id: "))
                ok = manager.complete_task(task_id)

                if ok:
                    print("Marked complete.")
                else:
                    print("Task not found.")

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("Invalid option.")

        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
