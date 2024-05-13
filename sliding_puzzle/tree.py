from collections import deque

from .puzzle import Puzzle


class Tree:
    def __init__(self, movement, puzzle: Puzzle, parent=None):
        self.movement = movement
        self.puzzle = puzzle
        self.children = puzzle.get_allowed_moves()
        self.parent = parent

        self.visited = False

    def create_child(self, i):
        """Expand a child of the current node."""
        p = Puzzle(board=self.puzzle.board.copy())
        p.move(self.children[i])

        self.children[i] = Tree(self.children[i], p, self)


def create_path(node):
    """Return the nodes from the starting position to the final solution.

    The nodes contain the movements made.
    """
    path = deque()
    path.append(node)

    while node.parent is not None:
        node = node.parent
        path.appendleft(node)

    return path
