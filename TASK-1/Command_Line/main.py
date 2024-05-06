class Task:
    def __init__(self, description, completed=False, priority=1, category=None, deadline=None, notes=None, labels=None):
        self.description = description
        self.completed = completed
        self.priority = priority
        self.category = category
        self.deadline = deadline
        self.notes = notes
        self.labels = labels

# Load tasks from a file (optional)
def load_tasks(user):
    tasks = []
    try:
        with open(f"{user}_tasks.txt", "r") as file:
            for line in file.readlines():
                description, status, priority, category, deadline, notes, labels = line.strip().split(",")
                tasks.append(Task(description, status == "True", int(priority), category, deadline, notes, labels))
    except FileNotFoundError:
        pass
    return tasks

# Save tasks to a file (optional)
def save_tasks(tasks, user):
    with open(f"{user}_tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task.description},{task.completed},{task.priority},{task.category},{task.deadline},{task.notes},{task.labels}\n")

# Main program loop
def main():
    user = input("Enter your username: ")
    tasks = load_tasks(user)

    while True:
        print("\n--- To-Do List ---")

        # List tasks
        for i, task in enumerate(tasks):
            status = "Completed" if task.completed else "Pending"
            print(f"{i+1}. Priority: {task.priority} - {status}: {task.description} - Category: {task.category} - Deadline: {task.deadline} - Notes: {task.notes} - Labels: {task.labels}")

        # User options
        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task Complete")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = int(input("Enter task priority (1-5, where 1 is the highest priority): "))
            category = input("Enter task category (optional): ")
            deadline = input("Enter task deadline (optional): ")
            notes = input("Enter task notes (optional): ")
            labels = input("Enter task labels (optional, comma-separated): ").split(",")
            tasks.append(Task(description, priority=priority, category=category, deadline=deadline, notes=notes, labels=labels))
        elif choice == "2":
            index = int(input("Enter task number to mark complete: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index].completed = True
            else:
                print("Invalid task number")
        elif choice == "3":
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                del tasks[index]
            else:
                print("Invalid task number")
        elif choice == "4":
            save_tasks(tasks, user)
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()