"""
Unit tests for astar_grid.py.
run this file directly to see your solver in action:
pytest 01_Informed_Search_A_Star/starter_code/test_astar_grid.py
"""
import pytest
from astar_grid import astar, find_cell


def test_case_1():
    """Category: Straight line / Open path."""
    grid = [
        "S...",
        "....",
        "....",
        "...G"
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")
    
    path, cost = astar(grid, start, goal)
    
    assert path is not None
    assert cost == 6  # 3 steps right + 3 steps down


def test_case_2():
    """Category: Unreachable goal (No path exists)."""
    grid = [
        "S..#",
        "...#",
        "####",
        "..#G"
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")
    
    path, cost = astar(grid, start, goal)
    
    assert path is None
    assert cost == float('inf')


def test_case_3():
    """Category: Wall detour / Obstacle navigation."""
    grid = [
        "S...",
        ".##.",
        ".##.",
        "...G"
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")
    
    path, cost = astar(grid, start, goal)
    
    assert path is not None
    assert cost == 6