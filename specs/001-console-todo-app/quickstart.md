# Quickstart Guide: Console Todo App

**Feature**: 001-console-todo-app
**Date**: 2026-01-02

## Setup

1. Ensure Python 3.13+ is installed on your system
2. Install dependencies using UV package manager:
   ```bash
   uv sync
   ```

## Running the Application

Run the console application:
```bash
python -m src.cli.main
```

## Basic Usage

### Adding a Todo
```
add "Task title here"
```

### Viewing All Todos
```
view
```

### Marking a Todo as Complete
```
complete 1
```

### Updating a Todo
```
update 1 "New title"
```

### Deleting a Todo
```
delete 1
```

## Example Workflow

1. Add a new todo: `add "Buy groceries"`
2. View all todos: `view`
3. Mark as complete: `complete 1`
4. View updated list: `view`