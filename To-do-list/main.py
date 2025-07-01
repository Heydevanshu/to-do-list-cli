FILENAME = "tasks.txt"

# ---- load tasks from file ----
def load_tasks():
    tasks = []
    try:
        with open(FILENAME, "r") as f:
            tasks = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        pass      # first run: file may not exist
    return tasks

# ---- save tasks list to file ----
def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for t in tasks:
            f.write(t + "\n")

# ---- main loop ----
tasks = load_tasks()

while True:
    print("\n===== TO-DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number 1-5")
        continue

    if choice == 1:  # view
        if not tasks:
            print("No tasks yet.")
        else:
            for idx, t in enumerate(tasks, 1):
                print(f"{idx}. {t}")

    elif choice == 2:  # add
        add = input("Enter new task: ").strip()
        if add:
            tasks.append(add)
            print("Task added!")

    elif choice == 3:  # complete
        if not tasks:
            print("No tasks to complete.")
            continue
        for idx, t in enumerate(tasks, 1):
            print(f"{idx}. {t}")
        try:
            done = int(input("Enter task number completed: "))
            tasks[done-1] = tasks[done-1] + "  [DONE]"
            print("Marked as completed.")
        except (ValueError, IndexError):
            print("Invalid number.")

    elif choice == 4:  # delete
        if not tasks:
            print("No tasks to delete.")
            continue
        for idx, t in enumerate(tasks, 1):
            print(f"{idx}. {t}")
        try:
            rem = int(input("Enter task number to delete: "))
            removed = tasks.pop(rem-1)
            print(f"Deleted: {removed}")
        except (ValueError, IndexError):
            print("Invalid number.")

    elif choice == 5:  # exit
        save_tasks(tasks)
        print("Tasks saved. Goodbye!")
        break

    else:
        print("Please choose between 1-5.")
