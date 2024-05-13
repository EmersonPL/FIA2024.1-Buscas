from collections import deque

from sliding_puzzle.tree import Tree, create_path


def breadth_search(puzzle):
    # starting node of the search tree
    tree = Tree((-1, -1), puzzle)

    if puzzle.is_solution():
        return create_path(tree)

    frontier = deque([tree])
    reached = {tree.puzzle.encode()}

    while frontier:
        node = frontier.popleft()

        for i, movement in enumerate(node.children):
            node.create_child(i)

            child = node.children[i]
            if child.puzzle.is_solution():
                return create_path(child)

            child_board = child.puzzle.encode()
            if child_board not in reached:
                reached.add(child_board)
                frontier.append(child)

    return None
