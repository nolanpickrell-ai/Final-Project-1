import csv
import os


class FileHandler:
    def __init__(self) -> None:
        os.makedirs("data", exist_ok=True)

    def save_vote(self, user_id: str, candidate: str) -> None:
        """Save a vote with user ID and candidate."""
        try:
            with open("data/votes.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([user_id, candidate])
        except Exception as e:
            raise IOError(f"Error saving vote: {str(e)}")

    def has_voted(self, user_id: str) -> bool:
        """Check if a user ID has already voted."""
        try:
            if not os.path.exists("data/votes.csv"):
                return False

            with open("data/votes.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == user_id:
                        return True
            return False
        except Exception as e:
            raise IOError(f"Error checking votes: {str(e)}")