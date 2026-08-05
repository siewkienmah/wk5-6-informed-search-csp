"""
Tests for astar_grid.py

Run with:
    pytest 01_Informed_Search_A_Star/starter_code/test_astar_grid.py -v
"""
import pytest
from astar_grid import astar, heuristic, neighbours, find_cell


# ---------------------------------------------------------------------
# GIVEN EXAMPLE -- complete, do not modify.
# Category: typical/normal small case.
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
    assert cost == 4


# ---------------------------------------------------------------------
# Test Case 1
# Category: typical/normal case with obstacles.
# This checks whether A* can find the shortest detour around walls.
# ---------------------------------------------------------------------
def test_case_1():
    grid = [
        "S#.",
        ".#.",
        "..G",
    ]

    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is not None
    assert path[0] == start
    assert path[-1] == goal
    assert cost == 4


# ---------------------------------------------------------------------
# Test Case 2
# Category: edge/boundary case.
# This checks whether the algorithm correctly handles start == goal.
# ---------------------------------------------------------------------
def test_case_2():
    grid = [
        "S",
    ]

    start = (0, 0)
    goal = (0, 0)

    path, cost = astar(grid, start, goal)

    assert path == [(0, 0)]
    assert cost == 0


# ---------------------------------------------------------------------
# Test Case 3
# Category: unsolvable case.
# This checks whether A* returns None and infinity when walls block
# every possible route to the goal.
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