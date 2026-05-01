"""
MainWindow module for the voting application.

This module handles the user interface and connects buttons
to the voting logic and file storage.
"""

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow

from models.vote_counter import VoteCounter
from services.file_handler import FileHandler


class MainWindow(QMainWindow):
    """
    Main window of the voting application.

    This class:
    - Loads the UI
    - Handles button clicks
    - Updates vote results
    - Connects logic and file storage
    """

    def __init__(self) -> None:
        """
        Initializes the main window and connects UI buttons.
        """
        super().__init__()

        uic.loadUi("gui/main_window.ui", self)

        self.vote_counter: VoteCounter = VoteCounter()
        self.file_handler: FileHandler = FileHandler()

        self.johnButton.clicked.connect(self.vote_john)
        self.janeButton.clicked.connect(self.vote_jane)
        self.exitButton.clicked.connect(self.close)

    def vote_john(self) -> None:
        """
        Handles voting for John.
        """
        self.process_vote("John")

    def vote_jane(self) -> None:
        """
        Handles voting for Jane.
        """
        self.process_vote("Jane")

    def process_vote(self, candidate: str) -> None:
        """
        Processes a vote for a candidate.

        Args:
            candidate (str): The selected candidate.
        """
        try:
            user_id: str = self.idInput.text().strip()

            if user_id == "":
                self.resultLabel.setText("Error: ID cannot be empty")
                return

            if self.file_handler.has_voted(user_id):
                self.resultLabel.setText("Error: You already voted")
                return

            if candidate == "John":
                self.vote_counter.vote_john()
            else:
                self.vote_counter.vote_jane()

            self.file_handler.save_vote(user_id, candidate)
            self.update_results()

        except Exception:
            self.resultLabel.setText("An error occurred")

    def update_results(self) -> None:
        """
        Updates the UI with the latest vote counts.
        """
        john_votes, jane_votes, total_votes = self.vote_counter.get_results()

        self.resultLabel.setText(
            f"John: {john_votes} | Jane: {jane_votes} | Total: {total_votes}"
        )