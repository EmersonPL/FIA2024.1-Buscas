from copy import deepcopy

import numpy as np

from searches.heuristics import NUM_OF_WRONG_PIECES_HEURISTIC


class Puzzle:
    board: np.ndarray

    def __init__(self, board=None, min_moves=5, max_moves=20):
        if board is None:
            self.board = np.array([[1, 2, 3], [4, 5, 6], [7, 8, -1]])
            self.empty = (2, 2)

            self.shuffle(min_moves, max_moves)
        else:
            self.board = board
            e = np.where(board == -1)
            self.empty = (e[0][0], e[1][0])

        self.initial_board = deepcopy(self.board)

    def encode(self):
        """Encode the board to a hashable format (string)."""
        return np.array2string(self.board.flatten(), separator='')

    def print_board(self):
        print(self.board)

    def restart(self):
        """Restart the board to it's initial configuration"""
        self.board = deepcopy(self.initial_board)

    def get_allowed_moves(self):
        """Return all allowed moves in the current configuration"""
        allowed_moves = []

        allowed_moves += self._get_vertical_moves()
        allowed_moves += self._get_horizontal_moves()

        return allowed_moves

    def _get_vertical_moves(self):
        allowed_moves = []
        if self.empty[0] > 0:
            allowed_moves.append((self.empty[0] - 1, self.empty[1]))  # down
        if self.empty[0] < len(self.board) - 1:
            allowed_moves.append((self.empty[0] + 1, self.empty[1]))  # up

        return allowed_moves

    def _get_horizontal_moves(self):
        allowed_moves = []
        if self.empty[1] > 0:
            allowed_moves.append((self.empty[0], self.empty[1] - 1))  # right
        if self.empty[1] < len(self.board) - 1:
            allowed_moves.append((self.empty[0], self.empty[1] + 1))  # left

        return allowed_moves

    def move(self, piece_to_move):
        """Move a piece, and update the empty position."""
        self.board[self.empty] = self.board[piece_to_move]
        self.board[piece_to_move] = -1

        self.empty = piece_to_move

    def is_solution(self):
        """Check if the current state is the solution."""
        if np.array_equal(
            self.board,
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, -1]])
        ):
            return True

        return False

    def shuffle(self, min_moves, max_moves):
        """Shuffle the board with a random number of moves.

        This can't just shuffle the puzzle matrix, as it can generate an
        impossible puzzle. Instead, just make random movements.
        """
        rng = np.random.default_rng()
        num_of_moves = rng.integers(min_moves, max_moves)

        for i in range(num_of_moves):
            allowed_moves = self.get_allowed_moves()
            move = rng.integers(0, len(allowed_moves))

            self.move(allowed_moves[move])

    def distance_to_solution(
        self, heuristic_to_use=NUM_OF_WRONG_PIECES_HEURISTIC
    ):
        # TODO: Add heuristics
        return np.sum(
            self.board != np.array([[1, 2, 3], [4, 5, 6], [7, 8, -1]])
        )
