"""
Tests for astar_grid.py

Run with:
    pytest 01_Informed_Search_A_Star/starter_code/test_astar_grid.py -v
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
# Mind-map Category: Obstacles / Navigation -> Detour required
# Why: Tests that A* correctly navigates around wall barriers and finds 
# the optimal path when direct linear paths are blocked.
# ---------------------------------------------------------------------
def test_case_1():
    grid = [
        "S..",
        "##.",
        "G..",
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is not None
    assert path[0] == start
    assert path[-1] == goal
    # Direct path straight down is blocked, must go around the wall:
    # (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (2,1) -> (2,0) = 6 moves
    assert cost == 6


# ---------------------------------------------------------------------
# Test Case 2
# Mind-map Category: Solvability -> Unsolvable / Completely blocked path
# Why: Ensures the algorithm terminates gracefully when the open set is 
# exhausted without reaching the goal, returning (None, inf).
# ---------------------------------------------------------------------
def test_case_2():
    grid = [
        "S#.",
        "##.",
        "..G",
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is None
    assert cost == float("inf")


# ---------------------------------------------------------------------
# Test Case 3
# Mind-map Category: Boundary / Edge Cases -> Start equals Goal
# Why: Tests trivial boundary behavior where start and goal are at the 
# exact same coordinate, requiring 0 moves and returning only the start node.
# ---------------------------------------------------------------------
def test_case_3():
    grid = [
        "S..",
    ]
    start = find_cell(grid, "S")
    goal = start  # Start is the goal

    path, cost = astar(grid, start, goal)

    assert path == [start]
    assert cost == 0


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))