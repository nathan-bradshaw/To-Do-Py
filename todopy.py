import os
import json
from datetime import datetime, timedelta
from prettytable import PrettyTable
import matplotlib.pyplot as plt

# Define the Task class to represent individual tasks
class Task:
    def __init__(self, task, category, due_date, priority):
        self.task = task
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def complete(self):
        self.completed = True

    def __str__(self):
        status = 'Done' if self.completed else 'Not Done'
        return f"[{self.created_at}] {self.task} - Category: {self.category}, Due: {self.due_date}, Priority: {self.priority}, Status: {status}"

# Define the ToDoList class to manage tasks
class ToDoList:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            # Load task data from JSON file if available
            with open(self.filename, 'r') as f:
                task_data = json.load(f)
                # Create Task instances from loaded data
                self.tasks = [Task(**task_info) for task_info in task_data]
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        # Prepare task data for saving to JSON file
        task_data = [{'task': task.task, 'category': task.category, 'due_date': task.due_date, 'priority': task.priority, 'completed': task.completed, 'created_at': task.created_at} for task in self.tasks]
        with open(self.filename, 'w') as f:
            # Save task data to JSON file
            json.dump(task_data, f, indent=4)

    def add_task(self, task, category, due_date, priority):
        # Add a new task to the list
        self.tasks.append(Task(task, category, due_date, priority))
        self.save_tasks()

    def list_tasks(self, sort_by=None):
        if sort_by:
            # Sort tasks based on specified attribute
            self.tasks.sort(key=lambda task: getattr(task, sort_by))
        return self.tasks

    def mark_completed(self, index):
        if 1 <= index <= len(self.tasks):
            # Mark task as completed at the specified index
            self.tasks[index - 1].complete()
            self.save_tasks()

    def remove_task(self, index):
        if 1 <= index <= len(self.tasks):
            # Remove task at the specified index
            self.tasks.pop(index - 1)
            self.save_tasks()

    def due_date_reminders(self):
        today = datetime.now().date()
        # Filter tasks due within the next day
        upcoming_tasks = [task for task in self.tasks if not task.completed and task.due_date and datetime.strptime(task.due_date, '%Y-%m-%d').date() <= today + timedelta(days=1)]
        return upcoming_tasks

    def filter_tasks_by_category(self, category):
        # Filter tasks based on the specified category
        filtered_tasks = [task for task in self.tasks if task.category.lower() == category.lower()]
        return filtered_tasks

    def priority_distribution(self):
        priorities = {}
        for task in self.tasks:
            if not task.completed:
                # Count tasks by priority level
                priorities[task.priority] = priorities.get(task.priority, 0) + 1
        return priorities

# Define function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main menu function for user interaction
def main_menu(todo_list):
    while True:
        clear_screen()
        print("ToDoPy - Task Manager")
        print("\nMenu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Completed")
        print("4. Remove Task")
        print("5. Due Date Reminders")  # Option for Due Date Reminders
        print("6. Filter by Category")
        print("7. Priority Distribution")
        print("8. Quit")

        choice = input("Select an option: ")

        if choice == '1':
            add_task_menu(todo_list)
        elif choice == '2':
            list_tasks_menu(todo_list)
        elif choice == '3':
            mark_completed_menu(todo_list)
        elif choice == '4':
            remove_task_menu(todo_list)
        elif choice == '5':
            due_date_reminders_menu(todo_list)  # Call the Due Date Reminders function
        elif choice == '6':
            filter_by_category_menu(todo_list)
        elif choice == '7':
            priority_distribution_menu(todo_list)
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Function to add a task
def add_task_menu(todo_list):
    clear_screen()
    task = input("Enter task: ")
    category = input("Enter category: ")
    due_date = input("Enter due date (YYYY-MM-DD), or leave empty: ")
    priority = input("Enter priority (Low, Medium, High): ")
    todo_list.add_task(task, category, due_date, priority)
    input("Task added. Press Enter to continue.")

# Function to list tasks
def list_tasks_menu(todo_list):
    clear_screen()
    sort_option = input("Sort by (due_date, priority, created_at) or press Enter for default order: ")
    tasks = todo_list.list_tasks(sort_option)
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        table = PrettyTable()
        table.field_names = ["#", "Task", "Category", "Due Date", "Priority", "Status"]
        for idx, task in enumerate(tasks, start=1):
            status = 'Done' if task.completed else 'Not Done'
            table.add_row([idx, task.task, task.category, task.due_date, task.priority, status])
        print(table)
    input("Press Enter to continue.")

# Function to mark a task as completed
def mark_completed_menu(todo_list):
    clear_screen()
    tasks = todo_list.list_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        table = PrettyTable()
        table.field_names = ["#", "Task", "Category", "Due Date", "Priority", "Status"]
        for idx, task in enumerate(tasks, start=1):
            status = 'Done' if task.completed else 'Not Done'
            table.add_row([idx, task.task, task.category, task.due_date, task.priority, status])
        print(table)
        index = int(input("Enter task number to mark as completed: "))
        todo_list.mark_completed(index)
        print("Task marked as completed.")
    input("Press Enter to continue.")

# Function to remove a task
def remove_task_menu(todo_list):
    clear_screen()
    tasks = todo_list.list_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        table = PrettyTable()
        table.field_names = ["#", "Task", "Category", "Due Date", "Priority", "Status"]
        for idx, task in enumerate(tasks, start=1):
            status = 'Done' if task.completed else 'Not Done'
            table.add_row([idx, task.task, task.category, task.due_date, task.priority, status])
        print(table)
        index = int(input("Enter task number to remove: "))
        todo_list.remove_task(index)
        print("Task removed.")
    input("Press Enter to continue.")

# Function to display due date reminders
def due_date_reminders_menu(todo_list):
    clear_screen()
    upcoming_tasks = todo_list.due_date_reminders()
    if not upcoming_tasks:
        print("No upcoming tasks.")
    else:
        print("Upcoming Tasks (Due within 1 day):")
        table = PrettyTable()
        table.field_names = ["#", "Task", "Category", "Due Date", "Priority"]
        for idx, task in enumerate(upcoming_tasks, start=1):
            table.add_row([idx, task.task, task.category, task.due_date, task.priority])
        print(table)
    input("Press Enter to continue.")

# Function to filter tasks by category
def filter_by_category_menu(todo_list):
    clear_screen()
    category = input("Enter category to filter by: ")
    filtered_tasks = todo_list.filter_tasks_by_category(category)
    if not filtered_tasks:
        print(f"No tasks found in category '{category}'.")
    else:
        print(f"Tasks in Category '{category}':")
        table = PrettyTable()
        table.field_names = ["#", "Task", "Category", "Due Date", "Priority", "Status"]
        for idx, task in enumerate(filtered_tasks, start=1):
            status = 'Done' if task.completed else 'Not Done'
            table.add_row([idx, task.task, task.category, task.due_date, task.priority, status])
        print(table)
    input("Press Enter to continue.")

# Function to display priority distribution
def priority_distribution_menu(todo_list):
    clear_screen()
    priorities = todo_list.priority_distribution()
    if not priorities:
        print("No tasks found.")
    else:
        print("Priority Distribution:")
        for priority, count in priorities.items():
            print(f"{priority}: {count} tasks")
        
        labels = list(priorities.keys())
        values = list(priorities.values())

        plt.figure(figsize=(8, 5))
        plt.bar(labels, values, color=['green', 'yellow', 'red'])
        plt.xlabel('Priority')
        plt.ylabel('Number of Tasks')
        plt.title('Priority Distribution')
        plt.tight_layout()
        plt.show()

    input("Press Enter to continue.")

# Entry point of the application
if __name__ == "__main__":
    # Initialize ToDoList with tasks from 'tasks.json'
    todo_list = ToDoList('tasks.json')
    # Launch the main menu for user interaction
    main_menu(todo_list)
