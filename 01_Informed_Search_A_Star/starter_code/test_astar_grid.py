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
from astar_grid import ASSIGNMENT_GRID, astar, heuristic, neighbours, find_cell


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
# Category: Structure -> complex (obstacles that force a detour) /
# Correctness -> optimality. Two wall rows each have a single gap, so the
# path is forced through two "bottleneck" cells. This checks that A* finds
# the true shortest route rather than a merely valid one.
# ---------------------------------------------------------------------
def test_case_1():
    grid = [
        "S....",
        "####.",
        ".....",
        ".####",
        "....G",
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is not None
    assert path[0] == start
    assert path[-1] == goal
    # Only route: (0,0)->(0,4) [4] ->(2,4) [2] ->(2,0) [4] ->(3,0) [1]
    # ->(4,0) [1] ->(4,4) [4] = 16 moves.
    assert cost == 16
    assert len(path) - 1 == cost  # path length matches reported cost


# ---------------------------------------------------------------------
# Test Case 2
# Category: Boundary Conditions -> start equals goal. astar() is called
# directly (not via S/G grid symbols, since a cell can't hold both) with
# start == goal to check the zero-length-path edge case is handled
# without error.
# ---------------------------------------------------------------------
def test_case_2():
    grid = [
        "...",
        "...",
        "...",
    ]
    start = goal = (1, 1)

    path, cost = astar(grid, start, goal)

    assert path == [start]
    assert cost == 0


# ---------------------------------------------------------------------
# Test Case 3
# Category: Solvability -> unsolvable / Correctness -> failure handling.
# The goal cell is completely enclosed by walls on all four sides, so no
# path can exist. Checks astar() reports failure correctly instead of
# crashing or returning a bogus path.
# ---------------------------------------------------------------------
def test_case_3():
    grid = [
        "S....",
        ".###.",
        ".#G#.",
        ".###.",
        ".....",
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is None
    assert cost == float("inf")


def test_assignment_grid():
    """The supplied assignment problem has the independently verified cost."""
    start = find_cell(ASSIGNMENT_GRID, "S")
    goal = find_cell(ASSIGNMENT_GRID, "G")

    # Direct coverage for the two required helper functions.
    assert heuristic(start, goal) == 13
    assert set(neighbours(ASSIGNMENT_GRID, start)) == {(0, 1), (1, 0)}

    path, cost = astar(ASSIGNMENT_GRID, start, goal)

    assert path is not None
    assert path[0] == start
    assert path[-1] == goal
    assert cost == 13
    assert len(path) - 1 == cost


def test_large_open_grid():
    # Category: Input Size -> large/stress. This exercises a substantially
    # larger search space than the six required cases.
    size = 30
    grid = ["." * size for _ in range(size)]
    start = (0, 0)
    goal = (size - 1, size - 1)

    path, cost = astar(grid, start, goal)

    assert path is not None
    assert cost == 2 * (size - 1)
    assert len(path) - 1 == cost


def test_diagonal_movement_bonus():
    grid = [
        "S..",
        "...",
        "..G",
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    assert heuristic(start, goal, allow_diagonal=True) == 2
    assert (1, 1) in set(neighbours(grid, start, allow_diagonal=True))

    path, cost = astar(grid, start, goal, allow_diagonal=True)

    assert path == [(0, 0), (1, 1), (2, 2)]
    assert cost == 2


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))
