from searches.breadth_search import breadth_search
from searches.depth_search import (
    depth_search,
    iterative_deepening_search,
    limited_depth_search,
)
from searches.heuristics import (
    MANHATTAN_DISTANCE_HEURISTIC,
    NUM_OF_WRONG_PIECES_HEURISTIC,
)
from searches.status import SearchStatus
from sliding_puzzle.puzzle import Puzzle
from sliding_puzzle.tree import create_path


def main():
    # puzzle = Puzzle(min_moves=50, max_moves=100)
    puzzle = Puzzle(min_moves=5, max_moves=10)

    print("Breadth search")
    breadth_path = breadth_search(puzzle)
    print_path(breadth_path, only_size=True)
    print()

    puzzle.restart()

    print("Depth search")
    original_depth_path = depth_search(puzzle)
    print_path(original_depth_path, only_size=True)
    print()

    puzzle.restart()

    print("Limited Depth search")
    limited_depth_path = limited_depth_search(puzzle, 10)
    print_path(limited_depth_path, only_size=True)
    print()

    puzzle.restart()

    #
    # puzzle.restart()
    # iterative_depth_path = depth_search(puzzle, "iterative_deepening")
    #
    # puzzle.restart()
    # a_star_path_manhattan = a_star_search(puzzle, MANHATTAN_DISTANCE_HEURISTIC)
    #
    # puzzle.restart()
    # a_star_path_num_wrong_pieces = a_star_search(
    #     puzzle,
    #     NUM_OF_WRONG_PIECES_HEURISTIC
    # )


def print_path(result, only_moves=True, only_size=False):
    if not result or result == SearchStatus.FAILURE:
        print(f"No solution found!")
        return

    path = create_path(result)
    print(f"Solution size: {len(path)}")

    if only_size:
        return

    for node in path:
        print(f"Movement: {node.movement}")
        if not only_moves:
            print(f"Current Board: ")
            node.puzzle.print_board()
            print("*"*80)

    print("*" * 80)


if __name__ == '__main__':
    main()
