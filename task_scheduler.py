print("""
1. Add Task
2. Complete Task
3. View Pending Tasks
4. View Next Task
5. Exit
""")

pending_tasks = []

def add_task():
    task = input("Enter the task description: ")
    pending_tasks.append(task)
    print(f"Task '{task}' added to the schedule.")

def complete_task():
    if pending_tasks:
        completed_task = pending_tasks.pop(0)
        print(f"Task '{completed_task}' marked as completed.")
    else:
        print("No pending tasks to complete.")

def view_pending_tasks():
    if pending_tasks:
        print("Pending Tasks:")
        for idx, task in enumerate(pending_tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("No pending tasks.")

def view_next_task():
    if pending_tasks:
        print(f"Next Task: {pending_tasks[0]}")
    else:
        print("No pending tasks.")

while True:
    choice = input("Choose an option (1-5): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        complete_task()
    elif choice == '3':
        view_pending_tasks()
    elif choice == '4':
        view_next_task()
    elif choice == '5':
        print("Exiting the task scheduler. Goodbye!")
        break
    else:
        print("Invalid option. Please choose a number between 1 and 5.")