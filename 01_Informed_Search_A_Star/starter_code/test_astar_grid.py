import pytest
from astar_grid import astar, heuristic, neighbours

def test_case_1_standard_path():
    """
    Mind-map branch: Standard / Clear Path with Obstacles
    Tests standard path finding around an obstacle wall.
    """
    grid = [
        "S...",
        ".#..",
        ".#..",
        "...G"
    ]
    start = (0, 0)
    goal = (3, 3)
    
    path, cost = astar(grid, start, goal)
    
    assert path is not None
    assert cost == 6
    assert path[0] == start
    assert path[-1] == goal


def test_case_2_unreachable_goal():
    """
    Mind-map branch: Unreachable / Blocked Goal
    Tests search behavior when no valid path exists to the goal.
    """
    grid = [
        "S.#.",
        "..#.",
        "###.",
        "...G"
    ]
    start = (0, 0)
    goal = (3, 3)
    
    path, cost = astar(grid, start, goal)
    
    assert path is None
    assert cost == float('inf')


def test_case_3_start_is_goal():
    """
    Mind-map branch: Edge Case - Start equals Goal
    Tests immediate termination when start and goal coordinates coincide.
    """
    grid = [
        "S...",
        "....",
        "....",
        "...."
    ]
    start = (0, 0)
    goal = (0, 0)
    
    path, cost = astar(grid, start, goal)
    
    assert path == [(0, 0)]
    assert cost == 0