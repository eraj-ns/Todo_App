# Data Model: Console Todo App

**Feature**: 001-console-todo-app
**Date**: 2026-01-02
**Input**: Feature specification and architecture plan

## Todo Entity

### Attributes
- **id**: Integer, unique identifier, auto-generated, required
- **title**: String, task title/description, required
- **description**: String, optional detailed description, nullable
- **status**: String, task status ("pending" or "completed"), default "pending"

### Example
```python
{
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, bread, eggs, fruits",
    "status": "pending"
}
```

## In-Memory Storage

### Structure
- Dictionary with ID as key and Todo object as value
- ID counter for generating unique IDs

### Operations
- Create: Add new todo to dictionary with auto-generated ID
- Read: Retrieve todo by ID or get all todos
- Update: Modify existing todo attributes
- Delete: Remove todo by ID