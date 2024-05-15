from collections import deque

from searches.status import SearchStatus
from sliding_puzzle.tree import Tree, create_path


# TODO: To be closer to the original algorithm, all depth-first searches
#  should not keep track of `reached`, using an `is-cycle` algorithm for loop
#  detection instead.
#  Maybe implement `is-cycle` by comparing the current node board with the
#  board of its parent (and all parents in the hierarchy, up to the root)?
def depth_search(puzzle):
    """Return the path to the solution, using a depth-first search.

    The search is a modified version of the depth-first search algorithm,
    which includes a detection of already visited nodes (as it usually would
    get in an infinite loop otherwise).
    """
    tree = Tree(movement=(-1, -1), puzzle=puzzle)

    frontier = deque([tree])
    reached = {tree.puzzle.encode()}

    while frontier:
        node = frontier.pop()

        if node.puzzle.is_solution():
            return node

        _expand_children(node, frontier, reached)

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
    """Return the path to the solution, using a depth-limited search.

    The search is a modified version of the depth-limited search algorithm,
    which includes a detection of already visited nodes (as it could get
    caught in an infinite loop otherwise).
    """
    tree = Tree(movement=(-1, -1), puzzle=puzzle)

    frontier = deque([tree])
    reached = {tree.puzzle.encode()}

    result = SearchStatus.FAILURE

    while frontier:
        node = frontier.pop()

        if node.puzzle.is_solution():
            return node

        if node.depth > depth_limit:
            result = SearchStatus.CUTOFF
        else:
            _expand_children(node, frontier, reached)

    return result


def _expand_children(node, frontier, reached):
    """Add all children of the node to the frontier and reached states set."""
    for i, child in enumerate(node.children):
        child = node.create_child(i)

        child_board = child.puzzle.encode()
        if child_board in reached:
            continue

        reached.add(child_board)
        frontier.append(child)
