"""
Tests for astar_grid.py

Run with:
    pytest 01_Informed_Search_A_Star/starter_code/test_astar_grid.py -v

`test_given_example` is the lecturer's given test.
The 3 custom test cases cover different categories:
1. Unsolvable / stress case
2. Typical / normal case
3. Maze / obstacle case
"""

from astar_grid import astar, find_cell, heuristic


def test_given_example():
    """Given Example: Test the assignment grid."""

    grid = [
        "S.......",
        ".#..#.#.",
        ".#....#.",
        ".###.##.",
        "...#....",
        "##.#.##.",
        ".....#..",
        ".##...G.",
    ]

    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is not None, "A path should exist in the assignment grid"
    assert cost == 13, f"Expected cost 13, got {cost}"
    assert path[0] == start, "Path must start at the start cell"
    assert path[-1] == goal, "Path must end at the goal cell"


def test_case_1():
    """Test Case 1: Unreachable Goal.

    Category: Unsolvable / Stress Case.
    Chosen to verify that A* correctly handles a goal that cannot be reached.
    """

    grid = [
        "S...#...",
        "....#...",
        "#####...",
        "....#G..",
    ]

    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is None, "Path should be None when goal is unreachable"
    assert cost == float("inf"), (
        "Cost should be float('inf') when goal is unreachable"
    )


def test_case_2():
    """Test Case 2: Open Grid / Direct Path.

    Category: Typical / Normal Case.
    Chosen to verify path reconstruction and correct cost on an open grid
    without obstacles.
    """

    grid = [
        "S...",
        "....",
        "....",
        "...G",
    ]

    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    expected_cost = 6

    assert path is not None, "A path should be found on an open grid"
    assert cost == expected_cost, (
        f"Expected cost {expected_cost}, got {cost}"
    )
    assert path[0] == start, "Path must start at the start cell"
    assert path[-1] == goal, "Path must end at the goal cell"
    assert len(path) == expected_cost + 1, (
        "Path length should equal cost + 1"
    )


def test_case_3():
    """Test Case 3: Maze Traversal and Heuristic Accuracy.

    Category: Edge / Obstacle Case.
    Chosen to verify that A* can navigate around walls while also checking
    that the Manhattan heuristic returns the correct distance.
    """

    # Verify Manhattan distance calculations.
    assert heuristic((0, 0), (3, 3)) == 6
    assert heuristic((1, 4), (5, 2)) == 6

    grid = [
        "S#...",
        ".#.#.",
        ".#.#.",
        "...#G",
    ]

    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is not None, "Path should be found around the walls"
    assert cost == 13, (
        f"Expected optimal path cost of 13, got {cost}"
    )
    assert path[0] == start, "Path must start at the start cell"
    assert path[-1] == goal, "Path must end at the goal cell"

    # Every consecutive pair of cells must be adjacent.
    for i in range(len(path) - 1):
        r1, c1 = path[i]
        r2, c2 = path[i + 1]

        assert grid[r1][c1] != "#", (
            f"Path includes a wall cell at {(r1, c1)}"
        )

        step_distance = abs(r1 - r2) + abs(c1 - c2)

        assert step_distance == 1, (
            f"Invalid non-adjacent step from {path[i]} to {path[i + 1]}"
        )