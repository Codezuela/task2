def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter a new task: ")
    tasks.append(task)

def print_tasks(tasks):
    """Print the current list of tasks."""
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def mark_completed(tasks):
    """Mark a task as completed."""
    if len(tasks) == 0:
        print("No tasks to mark as completed.")
        return
    num = int(input("Enter the task number to mark as completed: "))
    if num > 0 and num <= len(tasks):
        tasks[num-1] = f"{tasks[num-1]} (Completed)"
    else:
        print("Invalid task number.")

def delete_task(tasks):
    """Delete a task from the list."""
    if len(tasks) == 0:
        print("No tasks to delete.")
        return
    num = int(input("Enter the task number to delete: "))
    if num > 0 and num <= len(tasks):
        del tasks[num-1]
    else:
        print("Invalid task number.")

def show_help():
    """Print the help message."""
    print("To-do list application")
    print("Commands:")
    print("  add - Add a new task")
    print("  list - Print the current list of tasks")
    print("  completed - Mark a task as completed")
    print("  delete - Delete a task from the list")
    print("  help - Show this help message")

def main():
    """Main function to run the to-do list application."""
    tasks = []
    while True:
        command = input("Enter a command (add, list, completed, delete, help): ").lower()
        if command == "add":
            add_task(tasks)
        elif command == "list":
            print_tasks(tasks)
        elif command == "completed":
            mark_completed(tasks)
        elif command == "delete":
            delete_task(tasks)
        elif command == "help":
            show_help()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
