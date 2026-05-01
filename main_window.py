"""
Main window for the voting application.

This file handles the graphical user interface (GUI) and connects user actions
(button clicks) to the voting logic and file storage system.
"""

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from models.vote_counter import VoteCounter
from services.file_handler import FileHandler


class MainWindow(QMainWindow):
    """
    Main application window class.

    Responsible for:
    - Loading the Qt Designer UI
    - Handling button clicks
    - Updating vote results
    - Communicating with VoteCounter and FileHandler
    """

    def __init__(self) -> None:
        """Initialize the main window and set up event connections."""
        super().__init__()
        uic.loadUi("gui/main_window.ui", self)

        self.counter = VoteCounter()
        self.file_handler = FileHandler()

        # Button event connections
        self.johnButton.clicked.connect(self.vote_john)
        self.janeButton.clicked.connect(self.vote_jane)
        self.exitButton.clicked.connect(self.close)

    def vote_john(self) -> None:
        try:
            user_id = self.idInput.text().strip()

            if not user_id:
                raise ValueError("ID cannot be empty")

            if self.file_handler.has_voted(user_id):
                self.resultLabel.setText("Already voted")
                return

            self.counter.vote_john()
            self.file_handler.save_vote(user_id, "John")
            self.update_results()

        except Exception as e:
            self.resultLabel.setText(str(e))
    def vote_jane(self) -> None:
        try:
            user_id = self.idInput.text().strip()

            if not user_id:
                raise ValueError("ID cannot be empty")

            if self.file_handler.has_voted(user_id):
                self.resultLabel.setText("Already voted")
                return

            self.counter.vote_jane()
            self.file_handler.save_vote(user_id, "Jane")
            self.update_results()

        except Exception as e:
            self.resultLabel.setText(str(e))

    def update_results(self) -> None:
        """
        Update the result label with current vote totals.
        """
        john, jane, total = self.counter.get_results()
        self.resultLabel.setText(
            f"John: {john} | Jane: {jane} | Total: {total}"
        )