"""
Tests for astar_grid.py.

Run with:
    python -m pytest 01_Informed_Search_A_Star/starter_code/test_astar_grid.py -v
"""

from astar_grid import astar, heuristic, neighbours, find_cell


def test_given_example():
    """Test the normal example where a path exists."""
    grid = [
        "S..",
        "...",
        "..G",
    ]

    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is not None
    assert path[0] == start
    assert path[-1] == goal
    assert cost == 4
    assert len(path) == 5

    assert heuristic(start, goal) == 4

    assert set(neighbours(grid, start)) == {
        (0, 1),
        (1, 0),
    }


def test_case_1():
    """Edge case: start and goal are the same."""
    grid = ["S"]

    start = find_cell(grid, "S")
    goal = start

    path, cost = astar(grid, start, goal)

    assert path == [(0, 0)]
    assert cost == 0


def test_case_2():
    """Unsolvable case: a wall blocks the goal."""
    grid = ["S#G"]

    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is None
    assert cost == float("inf")


def test_case_3():
    """Obstacle case: the route must go around a wall."""
    grid = [
        "S#.",
        "...",
        "..G",
    ]

    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is not None
    assert path[0] == start
    assert path[-1] == goal
    assert cost == 4
    assert len(path) == 5
