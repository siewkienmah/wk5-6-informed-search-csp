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
# Mind-map category: Structure -> Obstacle Layout (Forced Detour / Wall Barrier)
# Why: Validates that A* correctly navigates around walls and obstacle barriers
# rather than attempting an invalid direct path or failing on non-linear paths.
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
    # Direct path is blocked by middle column walls; solver must go down column 0,
    # then right along row 2: (0,0) -> (1,0) -> (2,0) -> (2,1) -> (2,2)
    assert cost == 4


# ---------------------------------------------------------------------
# Test Case 2
# Mind-map category: Solvability -> Impossible / Completely Blocked Grid
# Why: Tests the algorithm's termination and safety behavior when no valid path
# exists. Ensures A* returns (None, float('inf')) without falling into infinite
# loops or raising unexpected errors.
# ---------------------------------------------------------------------
def test_case_2():
    grid = [
        "S.#.",
        "###.",
        "..#G",
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is None
    assert cost == float("inf")


# ---------------------------------------------------------------------
# Test Case 3
# Mind-map category: Boundary Conditions -> Degenerate Target (Start == Goal)
# Why: Tests edge case behavior where search start node and target goal node are identical.
# Ensures the cost is 0 and the path contains only the single starting coordinate.
# ---------------------------------------------------------------------
def test_case_3():
    grid = [
        "S..",
        "...",
        "..G",
    ]
    start = find_cell(grid, "S")

    # Pass the start node as both start and goal
    path, cost = astar(grid, start, start)

    assert path == [start]
    assert cost == 0


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))