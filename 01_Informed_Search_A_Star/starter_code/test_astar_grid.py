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
# Category: Boundary Conditions -> start equals goal (also Size ->
# trivial input). Chosen because it's a classic off-by-one trap: a
# correct A* must return a single-cell path of cost 0 without ever
# entering the main search loop's neighbour-expansion logic.
# ---------------------------------------------------------------------
def test_case_1_start_equals_goal():
    grid = [
        "S..",
        "...",
        "...",
    ]
    start = find_cell(grid, "S")

    path, cost = astar(grid, start, start)

    assert path == [start]
    assert cost == 0


# ---------------------------------------------------------------------
# Test Case 2
# Category: Structure -> complex (walls present) + Solvability ->
# solvable, checked against "What You're Actually Checking ->
# Optimality". Chosen because obstacles force the solver to route
# around walls instead of walking straight to the goal, and the
# expected cost is hand-computed in advance (see below) to confirm
# the path found is truly optimal, not just *a* path.
# ---------------------------------------------------------------------
def test_case_2_obstacles_optimal_path():
    grid = [
        "S...",
        ".##.",
        "....",
        "..#G",
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is not None
    assert path[0] == start
    assert path[-1] == goal
    # Hand-computed: Manhattan lower bound from (0,0) to (3,3) is 6, and
    # a valid route exists that achieves exactly 6
    # ((0,0)->(0,1)->(0,2)->(0,3)->(1,3)->(2,3)->(3,3)), so cost == 6
    # proves A* found the optimal path despite the walls.
    assert cost == 6


# ---------------------------------------------------------------------
# Test Case 3
# Category: Solvability -> unsolvable, checked against "What You're
# Actually Checking -> Failure handling". Chosen because the goal is
# completely enclosed by walls (unreachable from anywhere), so this
# verifies astar() reports failure correctly (None, inf) instead of
# crashing or returning a bogus path.
# ---------------------------------------------------------------------
def test_case_3_goal_sealed_off():
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


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))
