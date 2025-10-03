# Day 100: To-Do List Manager (CLI Final Project)

import json
import os

FILE = "todo.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("✅ No tasks yet!")
    else:
        print("\n📋 To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✔️" if task["done"] else "❌"
            print(f"{i}. {task['task']} [{status}]")
    print()

def add_task(tasks, task):
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"Added task: {task}")

def mark_done(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Marked as done: {tasks[index]['task']}")
    else:
        print("Invalid task number!")

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted task: {removed['task']}")
    else:
        print("Invalid task number!")

def menu():
    print("\n=== To-Do List Manager ===")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Quit")
    print("==========================")

if __name__ == "__main__":
    tasks = load_tasks()
    while True:
        menu()
        choice = input("Enter choice: ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            task = input("Enter new task: ").strip()
            if task:
                add_task(tasks, task)
        elif choice == "3":
            show_tasks(tasks)
            num = int(input("Enter task number to mark as done: ")) - 1
            mark_done(tasks, num)
        elif choice == "4":
            show_tasks(tasks)
            num = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, num)
        elif choice == "5":
            print("👋 Goodbye! Tasks saved.")
            break
        else:
            print("❌ Invalid choice, try again.")
