"""
Todo data model and in-memory storage for the console todo application.
"""
import json
import os
from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Todo:
    """
    Represents a single todo item with id, title, description, and status.
    """
    id: int
    title: str
    description: Optional[str] = None
    status: str = "pending"  # Can be "pending" or "completed"


class InMemoryTodoStore:
    """
    File-based storage mechanism for todos to persist between CLI sessions.
    """
    def __init__(self, storage_file: str = "todos.json"):
        self._storage_file = storage_file
        self._todos: Dict[int, Todo] = {}
        self._next_id: int = 1
        self._load_from_file()

    def _load_from_file(self):
        """Load todos from the storage file if it exists."""
        if os.path.exists(self._storage_file):
            try:
                with open(self._storage_file, 'r') as f:
                    data = json.load(f)
                    self._next_id = data.get('_next_id', 1)
                    todos_data = data.get('todos', {})
                    self._todos = {}
                    for todo_id, todo_data in todos_data.items():
                        todo_id = int(todo_id)  # Ensure key is int
                        self._todos[todo_id] = Todo(
                            id=todo_data['id'],
                            title=todo_data['title'],
                            description=todo_data.get('description'),
                            status=todo_data.get('status', 'pending')
                        )
            except (json.JSONDecodeError, KeyError):
                # If there's an error loading, start fresh
                self._todos = {}
                self._next_id = 1
        else:
            # Start fresh if file doesn't exist
            self._todos = {}
            self._next_id = 1

    def _save_to_file(self):
        """Save todos to the storage file."""
        data = {
            '_next_id': self._next_id,
            'todos': {str(todo_id): {
                'id': todo.id,
                'title': todo.title,
                'description': todo.description,
                'status': todo.status
            } for todo_id, todo in self._todos.items()}
        }
        with open(self._storage_file, 'w') as f:
            json.dump(data, f)

    def create_todo(self, title: str, description: Optional[str] = None) -> Todo:
        """Create a new todo with auto-generated ID."""
        todo = Todo(
            id=self._next_id,
            title=title,
            description=description,
            status="pending"
        )
        self._todos[todo.id] = todo
        self._next_id += 1
        self._save_to_file()
        return todo

    def get_todo(self, todo_id: int) -> Optional[Todo]:
        """Retrieve a todo by ID."""
        return self._todos.get(todo_id)

    def get_all_todos(self) -> List[Todo]:
        """Retrieve all todos."""
        return list(self._todos.values())

    def update_todo(self, todo_id: int, title: Optional[str] = None,
                   description: Optional[str] = None, status: Optional[str] = None) -> Optional[Todo]:
        """Update an existing todo."""
        if todo_id not in self._todos:
            return None

        todo = self._todos[todo_id]
        if title is not None:
            todo.title = title
        if description is not None:
            todo.description = description
        if status is not None:
            todo.status = status

        self._save_to_file()
        return todo

    def delete_todo(self, todo_id: int) -> bool:
        """Delete a todo by ID."""
        if todo_id in self._todos:
            del self._todos[todo_id]
            self._save_to_file()
            return True
        return False

    def mark_complete(self, todo_id: int) -> Optional[Todo]:
        """Mark a todo as complete."""
        if todo_id not in self._todos:
            return None

        todo = self._todos[todo_id]
        todo.status = "completed"
        self._save_to_file()
        return todo

    def mark_incomplete(self, todo_id: int) -> Optional[Todo]:
        """Mark a todo as incomplete."""
        if todo_id not in self._todos:
            return None

        todo = self._todos[todo_id]
        todo.status = "pending"
        self._save_to_file()
        return todo