# todo_app.py

def display_menu():
    print("Command Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Update task status")
    print("4. Exit")

def view_tasks():
    try:
        with open('tasks.txt', 'r') as f:
            tasks = f.readlines()
        if tasks:
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")
        else:
            print("No tasks found.")
    except FileNotFoundError:
        print("No tasks found.")

def add_task():
    task_description = input("Enter the task description: ")
    with open('tasks.txt', 'a') as f:
        f.write(f"{task_description}\n")
    print("Task added successfully!")

def update_task_status():
    view_tasks()
    task_number = int(input("Enter the task number to update its status: "))
    try:
        with open('tasks.txt', 'r') as f:
            tasks = f.readlines()
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1] = f"{tasks[task_number - 1].strip()} [Done]\n"
            with open('tasks.txt', 'w') as f:
                f.writelines(tasks)
            print("Task status updated successfully!")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks found.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task_status()
        elif choice == '4':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
