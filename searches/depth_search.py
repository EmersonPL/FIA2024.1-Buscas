from collections import deque

from sliding_puzzle.tree import Tree, create_path


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
            return create_path(node)

        for i, child in enumerate(node.children):
            node.create_child(i)
            child = node.children[i]

            # if child.puzzle.is_solution():
            #     return create_path(child)

            child_board = child.puzzle.encode()
            if child_board in reached:
                continue

            reached.add(child_board)
            frontier.append(child)

    return None
