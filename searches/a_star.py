from heapq import heappush, heappop
from typing import Callable, List

from searches.status import SearchStatus
from sliding_puzzle.puzzle import Puzzle
from sliding_puzzle.tree import Tree


def a_star_search(puzzle: Puzzle, heuristic: Callable):
    """Return the path to the solution, using a* search.

    Args:
        puzzle: The puzzle to solve.
        heuristic: A callable that receives a Puzzle object, and returns an int.
    """
    tree = Tree((-1, -1), puzzle, h=heuristic(puzzle))

    # Use a list of tuples, so the priority is automatically created.
    frontier: List[tree] = [tree]
    reached = {
        tree.puzzle.encode(): tree.a_star_cost
    }

    while frontier:
        node: Tree = heappop(frontier)
        if node.puzzle.is_solution():
            return node

        for i, movement in enumerate(node.children):
            child = node.create_child(i, h=heuristic(puzzle))
            child_board = child.puzzle.encode()

            if (
                child_board not in reached
                or child.a_star_cost < reached[child_board]
            ):
                reached[child_board] = child.a_star_cost
                heappush(frontier, child)

    return SearchStatus.FAILURE

