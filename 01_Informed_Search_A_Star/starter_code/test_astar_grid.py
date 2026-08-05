"""
Tests for astar_grid.py
"""
import pytest
from astar_grid import astar, find_cell


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


def test_case_1():
    grid = [
        "S..G",
        ".##.",
        "....",
        "...."
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")
    path, cost = astar(grid, start, goal)
    assert path is not None
    assert path[0] == start
    assert path[-1] == goal
    assert cost == 3


def test_case_2():
    grid = [
        "S##",
        "###",
        "##G"
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")
    path, cost = astar(grid, start, goal)
    assert path is None
    assert cost == float('inf')


def test_case_3():
    grid = [
        "S..",
        "...",
        "..."
    ]
    start = find_cell(grid, "S")
    goal = start
    path, cost = astar(grid, start, goal)
    assert path is not None
    assert path == [start]
    assert cost == 0


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))