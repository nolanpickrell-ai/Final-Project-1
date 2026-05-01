"""
FileHandler module for saving and reading vote data.

This module stores votes in a CSV file and checks
if a user has already voted.
"""

import csv
import os


class FileHandler:
    """
    Handles saving votes to a file and checking duplicate votes.
    """

    def __init__(self) -> None:
        """
        Creates the data folder if it does not exist.
        """
        os.makedirs("data", exist_ok=True)

    def save_vote(self, user_id: str, candidate: str) -> None:
        """
        Saves a vote to the CSV file.

        Args:
            user_id (str): The ID of the voter.
            candidate (str): The candidate chosen (John or Jane).
        """
        try:
            with open("data/votes.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([user_id, candidate])
        except Exception as error:
            raise IOError(f"Could not save vote: {error}")

    def has_voted(self, user_id: str) -> bool:
        """
        Checks if a user has already voted.

        Args:
            user_id (str): The ID of the voter.

        Returns:
            bool: True if user already voted, otherwise False.
        """
        try:
            if not os.path.exists("data/votes.csv"):
                return False

            with open("data/votes.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == user_id:
                        return True

            return False

        except Exception as error:
            raise IOError(f"Could not check votes: {error}")