from searches.breadth_search import breadth_search
from searches.depth_search import depth_search
from searches.heuristics import (
    MANHATTAN_DISTANCE_HEURISTIC,
    NUM_OF_WRONG_PIECES_HEURISTIC,
)
from sliding_puzzle.puzzle import Puzzle


def main():
    # puzzle = Puzzle(min_moves=50, max_moves=100)
    puzzle = Puzzle(min_moves=5, max_moves=10)

    breadth_path = breadth_search(puzzle)
    print_path(breadth_path, True)

    puzzle.restart()

    original_depth_path = depth_search(puzzle)
    print_path(original_depth_path, True)

    # puzzle.restart()
    # limited_depth_path = depth_search(puzzle, "limited_depth")
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


def print_path(path, only_moves=True):
    print(f"Solution size: {len(path)}")
    for node in path:
        print(f"Movement: {node.movement}")
        if not only_moves:
            print(f"Current Board: ")
            node.puzzle.print_board()
            print("*"*80)

    print("*" * 80)


if __name__ == '__main__':
    main()
