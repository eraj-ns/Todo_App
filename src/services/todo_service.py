"""
Todo service layer for business logic of the console todo application.
"""
from typing import List, Optional

from models.todo import InMemoryTodoStore, Todo


class TodoService:
    """
    Service class that handles business logic for todo operations.
    """
    def __init__(self):
        self.store = InMemoryTodoStore()

    def add_todo(self, title: str, description: Optional[str] = None) -> Todo:
        """
        Add a new todo task with validation for task title.
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        return self.store.create_todo(title.strip(), description)

    def get_all_todos(self) -> List[Todo]:
        """
        Get all todos from the store in a consistent order.
        """
        # Return todos sorted by their internal ID to maintain consistent ordering
        todos = self.store.get_all_todos()
        return sorted(todos, key=lambda x: x.id)

    def get_todo_by_sequence(self, seq_num: int) -> Optional[Todo]:
        """
        Get a specific todo by its sequence number (1-indexed).
        """
        todos = self.get_all_todos()
        if 1 <= seq_num <= len(todos):
            return todos[seq_num - 1]  # Convert 1-indexed to 0-indexed
        return None

    def get_todo_by_id(self, todo_id: int) -> Optional[Todo]:
        """
        Get a specific todo by internal ID.
        """
        return self.store.get_todo(todo_id)

    def get_sequence_number_by_id(self, todo_id: int) -> Optional[int]:
        """
        Get the sequence number for a given internal ID.
        """
        todos = self.get_all_todos()
        for i, todo in enumerate(todos):
            if todo.id == todo_id:
                return i + 1  # Convert 0-indexed to 1-indexed
        return None

    def update_todo_by_sequence(self, seq_num: int, title: Optional[str] = None,
                               description: Optional[str] = None, status: Optional[str] = None) -> Todo:
        """
        Update an existing todo by sequence number with validation.
        """
        # Get the todo by sequence number
        todos = self.get_all_todos()
        if not (1 <= seq_num <= len(todos)):
            raise ValueError(f"Todo with sequence number {seq_num} does not exist")

        todo = todos[seq_num - 1]
        todo_id = todo.id

        # Validate title if provided
        if title is not None and (not title or not title.strip()):
            raise ValueError("Task title cannot be empty")

        return self.store.update_todo(todo_id, title, description, status)

    def delete_todo_by_sequence(self, seq_num: int) -> bool:
        """
        Delete a todo by sequence number with validation.
        """
        todos = self.get_all_todos()
        if not (1 <= seq_num <= len(todos)):
            raise ValueError(f"Todo with sequence number {seq_num} does not exist")

        todo = todos[seq_num - 1]
        todo_id = todo.id

        return self.store.delete_todo(todo_id)

    def mark_complete_by_sequence(self, seq_num: int) -> Todo:
        """
        Mark a todo as complete by sequence number with validation.
        """
        todos = self.get_all_todos()
        if not (1 <= seq_num <= len(todos)):
            raise ValueError(f"Todo with sequence number {seq_num} does not exist")

        todo = todos[seq_num - 1]
        todo_id = todo.id

        result = self.store.mark_complete(todo_id)
        if result is None:
            raise ValueError(f"Failed to mark todo {seq_num} as complete")

        return result

    def mark_incomplete_by_sequence(self, seq_num: int) -> Todo:
        """
        Mark a todo as incomplete by sequence number with validation.
        """
        todos = self.get_all_todos()
        if not (1 <= seq_num <= len(todos)):
            raise ValueError(f"Todo with sequence number {seq_num} does not exist")

        todo = todos[seq_num - 1]
        todo_id = todo.id

        result = self.store.mark_incomplete(todo_id)
        if result is None:
            raise ValueError(f"Failed to mark todo {seq_num} as incomplete")

        return result