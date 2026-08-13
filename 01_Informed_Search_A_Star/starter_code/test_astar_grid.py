"""
Tests for astar_grid.py

Run with:
    pytest 01_Informed_Search_A_Star/starter_code/test_astar_grid.py -v

`test_given_example` below is COMPLETE -- study it as a template.

You must then write the 3 required test cases (test_case_1, test_case_2,
test_case_3). Read ../../03_Test_Case_Design/mindmap.md and
training_guide.md before choosing what your 3 cases should cover. Aim to
pick 3 *different* categories (e.g. one typical/normal case, one
edge/boundary case, one unsolvable-or-stress case) rather than 3 variations
of the same thing.

For each test case, write a short comment explaining WHICH category from
the mind-map it represents and WHY you chose it.
"""
import pytest
from astar_grid import astar, heuristic, neighbours, find_cell


# ---------------------------------------------------------------------
# GIVEN EXAMPLE -- complete, do not modify. Use this as your template.
# Category: typical/normal small case (from the mind-map: "Structure ->
# straightforward, no obstacles").
# ---------------------------------------------------------------------
def test_given_example():
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
    # Shortest possible Manhattan path on an open 3x3 grid is 4 moves.
    assert cost == 4


# ---------------------------------------------------------------------
# Test Case 1
# Category: typical/normal case with obstacles (Structure -> path exists
# but must navigate around walls). Chosen because the given example has
# no obstacles; this verifies the solver correctly avoids walls and still
# finds a shortest path.
# ---------------------------------------------------------------------
def test_case_1():
    grid = [
        "S..#",
        ".#..",
        "..#G",
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is not None
    assert path[0] == start
    assert path[-1] == goal
    # Optimal path length on this grid is 5
    assert cost == 5
    # Every step must be walkable and adjacent
    for i in range(len(path) - 1):
        r1, c1 = path[i]
        r2, c2 = path[i + 1]
        assert abs(r1 - r2) + abs(c1 - c2) == 1
        assert grid[r2][c2] != "#"


# ---------------------------------------------------------------------
# Test Case 2
# Category: edge/boundary case — start is adjacent to goal (or start == goal
# style minimal distance). Chosen to exercise the base case where the open
# list immediately pops the goal after zero or one expansion, and to check
# that cost == 0 when start == goal.
# ---------------------------------------------------------------------
def test_case_2():
    # Sub-case A: start == goal
    grid_same = [
        "S",
    ]
    # Manually treat the single cell as both start and goal
    start = (0, 0)
    goal = (0, 0)
    path, cost = astar(grid_same, start, goal)
    assert path == [start]
    assert cost == 0

    # Sub-case B: start immediately adjacent to goal (boundary of path length)
    grid_adj = [
        "SG",
    ]
    start = find_cell(grid_adj, "S")
    goal = find_cell(grid_adj, "G")
    path, cost = astar(grid_adj, start, goal)
    assert path is not None
    assert path[0] == start
    assert path[-1] == goal
    assert cost == 1
    assert len(path) == 2


# ---------------------------------------------------------------------
# Test Case 3
# Category: unsolvable / no-path case (negative / failure case).
# Chosen because a correct A* implementation must detect when the open
# list empties without ever popping the goal and return (None, inf).
# ---------------------------------------------------------------------
def test_case_3():
    grid = [
        "S#G",
        "###",
        "...",
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is None
    assert cost == float("inf")


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))