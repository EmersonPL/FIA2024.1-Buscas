from collections import deque

from searches.status import SearchStatus
from sliding_puzzle.tree import Tree


def depth_search(puzzle):
    """Return the path to the solution, using a depth-first search."""
    tree = Tree(movement=(-1, -1), puzzle=puzzle)

    frontier = deque([tree])

    while frontier:
        node = frontier.pop()

        if node.puzzle.is_solution():
            return node

        _expand_children(node, frontier)

    return None


def iterative_deepening_search(puzzle):
    """Return the path to the solution, using an iterative deepening search."""
    result = SearchStatus.CUTOFF

    i = 0
    while result == SearchStatus.CUTOFF:
        result = limited_depth_search(puzzle, i)
        i += 1

    return result


def limited_depth_search(puzzle, depth_limit: int) -> Tree | SearchStatus:
    """Return the path to the solution, using a depth-limited search."""
    tree = Tree(movement=(-1, -1), puzzle=puzzle)

    frontier = deque([tree])

    result = SearchStatus.FAILURE

    while frontier:
        node = frontier.pop()

        if node.puzzle.is_solution():
            return node

        if node.depth >= depth_limit:
            result = SearchStatus.CUTOFF
        else:
            _expand_children(node, frontier)

    return result


def _expand_children(node, frontier):
    """Add all children of the node to the frontier and reached states set."""
    for i, child in enumerate(node.children):
        child = node.create_child(i)

        if _is_cycle(child):
            continue

        frontier.append(child)


def _is_cycle(node: Tree) -> bool:
    board = node.puzzle.encode()
    while True:
        if node.parent is None:
            return False

        parent = node.parent

        if board == parent.puzzle.encode():
            return True

        node = parent
