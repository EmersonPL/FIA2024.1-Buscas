from collections import deque

from .puzzle import Puzzle


class Tree:
    def __init__(self, movement, puzzle: Puzzle, parent=None, h=0):
        self.movement = movement
        self.puzzle = puzzle
        self.children = puzzle.get_allowed_moves()
        self.parent = parent

        self.depth = 0 if parent is None else parent.depth + 1
        self.visited = False

        self.a_star_cost = self.depth + h

    def __lt__(self, other):
        return self.a_star_cost < other.a_star_cost

    def __le__(self, other):
        return self.a_star_cost <= other.a_star_cost

    def __gt__(self, other):
        return self.a_star_cost > other.a_star_cost

    def __ge__(self, other):
        return self.a_star_cost >= other.a_star_cost

    def create_child(self, i, h: int = 0):
        """Expand a child of the current node."""
        p = Puzzle(board=self.puzzle.board.copy())
        p.move(self.children[i])

        return Tree(self.children[i], p, self, h=h)


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
