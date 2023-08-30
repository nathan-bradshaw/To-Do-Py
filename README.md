# ToDoPy - Advanced Task Management Console Application

ToDoPy is an advanced task management console application written in Python. It provides a comprehensive set of features to efficiently organize and manage your tasks. With a user-friendly interface and powerful functionalities, ToDoPy streamlines your task management process.

## Features

### 1. Add Tasks

You can easily add new tasks to your task list using the "Add Task" option. When adding a task, you need to provide the following details:

- **Task Name**: Enter the name or description of the task.
- **Category**: Specify the category or type of the task.
- **Due Date**: Enter the due date for the task in the format YYYY-MM-DD. This is optional and can be left empty.
- **Priority**: Assign a priority level to the task: "Low," "Medium," or "High."

### 2. List Tasks

The "List Tasks" option allows you to view your tasks in a tabular format. You can choose to sort the tasks based on different attributes, including:

- **Due Date**: Tasks are sorted based on their due dates in ascending order.
- **Priority**: Tasks are sorted by their priority levels (Low, Medium, High).
- **Creation Date**: Tasks are sorted based on their creation dates in ascending order.

This sorted view helps you get a quick overview of your tasks and make informed decisions.

### 3. Mark Completed

With the "Mark Completed" option, you can mark tasks as completed. When you select a task and mark it as completed, the application updates the task's status accordingly. This feature allows you to track your progress and keep your task list up to date.

### 4. Remove Task

The "Remove Task" option enables you to remove tasks from your list. You can select a task to remove, and the application will delete it from the list. This feature helps you manage your task list and keep it organized.

### 5. Due Date Reminders

The "Due Date Reminders" option provides you with a list of tasks that are due within the next day. This reminder helps you stay on top of tasks with approaching deadlines, allowing you to manage your time effectively.

### 6. Filter by Category

You can use the "Filter by Category" option to view tasks from a specific category. After entering a category name, the application will display tasks that belong to that category. This feature is useful for focusing on specific types of tasks.

### 7. Priority Distribution

The "Priority Distribution" option allows you to visualize the distribution of tasks based on their priority levels. The application generates an interactive bar chart that displays the number of tasks in each priority category (Low, Medium, High). This visualization provides insights into your task priorities at a glance.

## Getting Started

To run ToDoPy on your local machine, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory using the terminal.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the application with `python todo.py`.

Follow the on-screen menu prompts to explore and utilize the various features of the application.

## Dependencies

- `prettytable`: Used to display tasks in a tabular format.
- `matplotlib`: Used to generate priority distribution visualizations.

## Contributions

Contributions to ToDoPy are welcome! If you want to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and document the code.
4. Submit a pull request detailing your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
