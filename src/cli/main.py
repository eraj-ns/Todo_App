"""
Main menu-driven CLI application for the console todo application.
"""
import sys
import os
# Add the src directory to the path so we can import from services and models
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.todo_service import TodoService


class TodoApp:
    """
    Main application class that provides a menu-driven interface for the todo app.
    """
    def __init__(self):
        self.service = TodoService()

    def display_menu(self):
        """Display the main menu."""
        print("\nWelcome to the Todo Application!\n")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Mark Task Incomplete")
        print("7. Exit")
        print()

    def get_user_choice(self):
        """Get and validate user's menu choice."""
        try:
            choice = input("Enter your choice (1-7): ").strip()
            if choice in ['1', '2', '3', '4', '5', '6', '7']:
                return int(choice)
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
                return None
        except KeyboardInterrupt:
            print("\n\nExiting application...")
            return 7
        except Exception:
            print("Invalid choice. Please enter a number between 1 and 7.")
            return None

    def add_task(self):
        """Add a new task."""
        title = input("Enter task title: ").strip()
        if not title:
            print("Task title cannot be empty.")
            return

        try:
            todo = self.service.add_todo(title)
            print(f"Task added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def view_tasks(self):
        """View all tasks."""
        todos = self.service.get_all_todos()

        if not todos:
            print("No tasks found.")
            return

        print("\nYour Tasks:")
        for i, todo in enumerate(todos, 1):
            status = "X" if todo.status == "completed" else " "
            print(f"{i}. [{status}] {todo.title}")

    def get_task_id(self, action):
        """Get and validate task ID from user."""
        try:
            task_id_input = input(f"Enter task ID to {action}: ").strip()
            if not task_id_input.isdigit():
                print("Error: Task ID must be a number.")
                return None
            task_id = int(task_id_input)

            todos = self.service.get_all_todos()
            if task_id < 1 or task_id > len(todos):
                print("Error: Task ID does not exist.")
                return None

            return task_id
        except ValueError:
            print("Error: Task ID must be a number.")
            return None

    def update_task(self):
        """Update an existing task."""
        task_id = self.get_task_id("update")
        if task_id is None:
            return

        new_title = input("Enter new task title: ").strip()
        if not new_title:
            print("Task title cannot be empty.")
            return

        try:
            self.service.update_todo_by_sequence(task_id, title=new_title)
            print("Task updated successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def delete_task(self):
        """Delete a task."""
        task_id = self.get_task_id("delete")
        if task_id is None:
            return

        try:
            self.service.delete_todo_by_sequence(task_id)
            print("Task deleted successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def mark_complete(self):
        """Mark a task as complete."""
        task_id = self.get_task_id("mark complete")
        if task_id is None:
            return

        try:
            self.service.mark_complete_by_sequence(task_id)
            print("Task marked as complete!")
        except ValueError as e:
            print(f"Error: {e}")

    def mark_incomplete(self):
        """Mark a task as incomplete."""
        task_id = self.get_task_id("mark incomplete")
        if task_id is None:
            return

        try:
            self.service.mark_incomplete_by_sequence(task_id)
            print("Task marked as incomplete!")
        except ValueError as e:
            print(f"Error: {e}")

    def run(self):
        """Run the main application loop."""
        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == 1:
                self.add_task()
            elif choice == 2:
                self.view_tasks()
            elif choice == 3:
                self.update_task()
            elif choice == 4:
                self.delete_task()
            elif choice == 5:
                self.mark_complete()
            elif choice == 6:
                self.mark_incomplete()
            elif choice == 7:
                print("Goodbye!")
                break

            # Pause to let user see the result before showing menu again
            input("\nPress Enter to continue...")


def main():
    """
    Application entry point.
    """
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()