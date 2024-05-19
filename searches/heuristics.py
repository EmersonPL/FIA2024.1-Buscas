import numpy as np

from sliding_puzzle.puzzle import Puzzle


def num_of_wrong_pieces_heuristic(puzzle: Puzzle) -> int:
    """Return the distance to the solution as the number of pieces not in place
    """
    return np.sum(
        puzzle.board != np.array([[1, 2, 3], [4, 5, 6], [7, 8, -1]])
    )


def manhattan_distance_heuristic(puzzle: Puzzle) -> int:
    """Return the distance to the solution as a manhattan distance.

    The distance returns the sum of the number of movements that each piece
    must make in order to be in the correct place (ignoring every place that
    it needs to displace)
    """
    expected_positions = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        -1: (2, 2),
    }

    distance = 0
    for i in range(0, len(puzzle.board)):
        for j in range(0, len(puzzle.board[i])):
            value = puzzle.board.item(i, j)
            distance += abs(i - expected_positions[value][0])
            distance += abs(j - expected_positions[value][1])

    return distance
