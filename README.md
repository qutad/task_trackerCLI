# Task Tracker CLI

A lightweight, terminal-based task management system built with Python. This tool allows you to track your daily goals, update their progress, and store them persistently in a local JSON file.



## Features

* **Persistent Storage:** Tasks are saved to `tasks.json`, so your data persists even after closing the program.
* **CRUD Operations:** Create, Read, Update, and Delete tasks with simple menu prompts.
* **Status Filtering:** View all tasks or filter them by `todo`, `in-progress`, or `done`.
* **Input Validation:** Includes basic error handling for invalid ID entries.



##  Getting Started

### Prerequisites
* **Python 3.x** installed on your system.

### Installation & Execution
1.  **Download the script:** Save the code as `task_tracker.py`.
2.  **Run the application:**
    ```bash
    python task_tracker.py
    ```



##  How to Use

When you run the script, you will be presented with a menu. Simply enter the number corresponding to your desired action:

| Option | Action | Description |
| :--- | :--- | :--- |
| **1** | **Add Task** | Enter a description; the task defaults to `todo`. |
| **2** | **List All** | Displays every task currently in the system. |
| **3** | **Filter** | Show tasks by specific status (`done`, `todo`, `in-progress`). |
| **4** | **Update** | Change a task's status by entering its unique ID. |
| **5** | **Delete** | Remove a task from the database using its ID. |
| **q / quit** | **Exit** | Safely close the application. |



##  Data Storage

The application automatically creates a `tasks.json` file in the same directory. The data is structured as follows:

```json
[
    {
        "id": 1,
        "description": "Clean the kitchen",
        "status": "todo"
    },
    {
        "id": 2,
        "description": "Read Python documentation",
        "status": "in-progress"
    }
]
