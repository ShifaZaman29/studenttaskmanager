import json
import os


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename) as f:
                self.tasks = json.load(f)

    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, title):
        task_id = max([t["id"] for t in self.tasks], default=0) + 1
        task = {"id": task_id, "title": title, "done": False}
        self.tasks.append(task)
        self.save()
        return task
    
    def list_tasks(self):
        return self.tasks


    def show_tasks(self):
        tasks = self.list_tasks()
        if not tasks:
            print("No tasks yet.")
        for t in tasks:
            status = "[x]" if t["done"] else "[ ]"
        print(f"{t['id']}. {status} {t['title']}")
    
    