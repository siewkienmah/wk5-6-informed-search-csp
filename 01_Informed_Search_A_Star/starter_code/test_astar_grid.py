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
# Category: Structure -> Obstacles requiring detour (Typical case).
# Why I chose it: The heuristic (Manhattan distance) will naturally pull 
# the search to the right, but a wall blocks it. This tests if the algorithm 
# can correctly "give up" the greedy path, detour around the wall, and 
# eventually find the goal.
# ---------------------------------------------------------------------
def test_case_1():
    grid = [
        "S#..",
        ".#..",
        ".#..",
        "...G"
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is not None
    assert path[0] == start
    assert path[-1] == goal
    # To get around the wall: 3 steps down, 3 steps right. Total cost = 6.
    assert cost == 6


# ---------------------------------------------------------------------
# Test Case 2
# Category: Edge Cases -> Unreachable Goal / No path.
# Why I chose it: Tests the termination condition of the algorithm when it 
# is impossible to reach the goal. It ensures that the priority queue 
# empties gracefully and the function returns None and float('inf') instead 
# of getting stuck in an infinite loop.
# ---------------------------------------------------------------------
def test_case_2():
    grid = [
        "S...",
        "...#",
        "..#G",
        "...#"
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is None
    assert cost == float('inf')


# ---------------------------------------------------------------------
# Test Case 3
# Category: Structure -> Heuristic Trap / U-shaped corridor (Stress case).
# Why I chose it: S and G are physically adjacent, meaning the heuristic 
# is initially very small (h=2). However, a long horizontal wall separates 
# them, forcing the algorithm to explore almost the entire grid to go around. 
# This rigorously tests the closed_set logic.
# ---------------------------------------------------------------------
def test_case_3():
    grid = [
        "S.......",
        "#######.",
        "G.......",
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is not None
    # S moves right 7 times, down 2 times, left 7 times to reach G. Total = 16.
    assert cost == 16

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))
