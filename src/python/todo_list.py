class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True

    def show_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "[x]" if task["completed"] else "[ ]"
            print(f"{i}. {status} {task['task']}")

if __name__ == "__main__":
    todo = TodoList()
    todo.add_task("Buy groceries")
    todo.add_task("Walk the dog")
    todo.show_tasks()
    todo.complete_task(0)
    print("\nAfter completing first task:")
    todo.show_tasks()
