# Console Todo Application

A simple, in-memory console-based todo application built with Python.

## Features

- Add new todo tasks
- View all todo tasks
- Mark tasks as complete
- Update existing tasks
- Delete tasks
- In-memory storage (no persistence)

## Requirements

- Python 3.13+

## Installation

No installation required. The application runs directly from source.

## Usage

```bash
# Add a new todo
python src/cli/main.py add "Task title here"

# View all todos
python src/cli/main.py view

# Mark a todo as complete
python src/cli/main.py complete 1

# Update a todo
python src/cli/main.py update 1 "New title for task"

# Delete a todo
python src/cli/main.py delete 1

# Show help
python src/cli/main.py help
```

## Example Workflow

1. Add a new todo: `python src/cli/main.py add "Buy groceries"`
2. View all todos: `python src/cli/main.py view`
3. Mark as complete: `python src/cli/main.py complete 1`
4. View updated list: `python src/cli/main.py view`

## Architecture

The application follows a layered architecture:
- **CLI Layer**: Handles user input and output (`src/cli/main.py`)
- **Service Layer**: Contains business logic (`src/services/todo_service.py`)
- **Model Layer**: Defines data structures and in-memory storage (`src/models/todo.py`)