"""
VoteCounter module for the voting application.

This class handles all voting logic, including tracking votes
for each candidate and returning current results.
"""


class VoteCounter:
    """
    A simple class to manage vote counting for two candidates.
    """

    def __init__(self) -> None:
        """
        Initialize vote counts for John and Jane.
        """
        self._john_votes: int = 0
        self._jane_votes: int = 0

    def vote_john(self) -> None:
        """
        Increment the vote count for John.
        """
        self._john_votes += 1

    def vote_jane(self) -> None:
        """
        Increment the vote count for Jane.
        """
        self._jane_votes += 1

    def get_results(self) -> tuple[int, int, int]:
        """
        Get the current voting results.

        Returns:
            tuple[int, int, int]: A tuple containing:
                - John votes
                - Jane votes
                - Total votes
        """
        total = self._john_votes + self._jane_votes
        return self._john_votes, self._jane_votes, total