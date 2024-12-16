from typing import List, Optional
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QTextEdit, QWidget

class Task:
    def __init__(self, title: str, description: str, completed: bool = False):
        self.title = title
        self.description = description
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def __repr__(self):
        return f"Task(title='{self.title}', completed={self.completed})"


class TodoManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, title: str, description: str) -> Task:
        task = Task(title, description)
        self.tasks.append(task)
        return task

    def remove_task(self, title: str) -> bool:
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return True
        return False

    def find_task(self, title: str) -> Optional[Task]:
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def list_tasks(self) -> List[Task]:
        return self.tasks

    def mark_task_complete(self, title: str) -> bool:
        task = self.find_task(title)
        if task:
            task.mark_complete()
            return True
        return False

    def clear_completed(self):
        self.tasks = [task for task in self.tasks if not task.completed]


class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.manager = TodoManager()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Todo Manager")

        layout = QVBoxLayout()

        self.task_list = QListWidget()
        layout.addWidget(self.task_list)

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Task Title")
        layout.addWidget(self.title_input)

        self.description_input = QTextEdit()
        self.description_input.setPlaceholderText("Task Description")
        layout.addWidget(self.description_input)

        add_button = QPushButton("Add Task")
        add_button.clicked.connect(self.add_task)
        layout.addWidget(add_button)

        remove_button = QPushButton("Remove Task")
        remove_button.clicked.connect(self.remove_task)
        layout.addWidget(remove_button)

        complete_button = QPushButton("Mark Complete")
        complete_button.clicked.connect(self.mark_task_complete)
        layout.addWidget(complete_button)

        clear_button = QPushButton("Clear Completed")
        clear_button.clicked.connect(self.clear_completed)
        layout.addWidget(clear_button)

        self.setLayout(layout)

    def refresh_task_list(self):
        self.task_list.clear()
        for task in self.manager.list_tasks():
            self.task_list.addItem(f"{'[X]' if task.completed else '[ ]'} {task.title}: {task.description}")

    def add_task(self):
        title = self.title_input.text()
        description = self.description_input.toPlainText()
        if title:
            self.manager.add_task(title, description)
            self.refresh_task_list()
            self.title_input.clear()
            self.description_input.clear()

    def remove_task(self):
        selected_items = self.task_list.selectedItems()
        if selected_items:
            title = selected_items[0].text().split(':')[0][4:].strip()
            self.manager.remove_task(title)
            self.refresh_task_list()

    def mark_task_complete(self):
        selected_items = self.task_list.selectedItems()
        if selected_items:
            title = selected_items[0].text().split(':')[0][4:].strip()
            self.manager.mark_task_complete(title)
            self.refresh_task_list()

    def clear_completed(self):
        self.manager.clear_completed()
        self.refresh_task_list()


if __name__ == "__main__":
    app = QApplication([])
    todo_app = TodoApp()
    todo_app.show()
    app.exec_()
