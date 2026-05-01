"""
VoteCounter module for the voting application.

This module keeps track of votes for each candidate
and calculates total votes.
"""


class VoteCounter:
    """
    A class used to count votes for two candidates: John and Jane.
    """

    def __init__(self) -> None:
        """
        Creates a new VoteCounter with zero votes for both candidates.
        """
        self._john_votes: int = 0
        self._jane_votes: int = 0

    def vote_john(self) -> None:
        """
        Adds one vote to John.
        """
        self._john_votes += 1

    def vote_jane(self) -> None:
        """
        Adds one vote to Jane.
        """
        self._jane_votes += 1

    def get_results(self) -> tuple[int, int, int]:
        """
        Gets the current vote totals.

        Returns:
            tuple[int, int, int]: John votes, Jane votes, and total votes.
        """
        total_votes: int = self._john_votes + self._jane_votes
        return self._john_votes, self._jane_votes, total_votes