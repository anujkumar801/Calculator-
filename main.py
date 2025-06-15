import os

FILENAME = "todo.txt"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    print("\n📝 Your To-Do List:")
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added.")

def update_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_task = input("Enter updated task: ")
            tasks[index] = new_task
            save_tasks(tasks)
            print("✏️ Task updated.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks(tasks)
            print("🗑️ Task deleted.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n📌 TO-DO LIST MENU:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
