"""
Tests for csp_map_coloring.py

Run with:
    pytest 02_CSP/starter_code/test_csp_map_coloring.py -v
"""
import pytest
from csp_map_coloring import backtracking_search, is_consistent


def _is_valid_solution(solution, variables, neighbours):
    """Check a solution assigns every variable and breaks no constraints."""
    if solution is None:
        return False

    if set(solution.keys()) != set(variables):
        return False

    for var, value in solution.items():
        for neighbour in neighbours[var]:
            if neighbour in solution and solution[neighbour] == value:
                return False

    return True


# ---------------------------------------------------------------------
# GIVEN EXAMPLE -- complete, do not modify.
# Category: typical/normal small solvable case.
# ---------------------------------------------------------------------
def test_given_example():
    from csp_map_coloring import VARIABLES, NEIGHBOURS, DOMAIN

    solution = backtracking_search(VARIABLES, DOMAIN)

    assert solution is not None
    assert _is_valid_solution(solution, VARIABLES, NEIGHBOURS)


# ---------------------------------------------------------------------
# Test Case 1
# Category: constraint/invalid assignment case.
# This checks that the same colour is rejected for adjacent regions.
# ---------------------------------------------------------------------
def test_case_1():
    assignment = {
        "WA": "Red"
    }

    assert is_consistent(assignment, "NT", "Red") is False
    assert is_consistent(assignment, "NT", "Green") is True


# ---------------------------------------------------------------------
# Test Case 2
# Category: edge/boundary case.
# Tasmania has no neighbours, so every colour should be consistent.
# ---------------------------------------------------------------------
def test_case_2():
    assignment = {
        "WA": "Red",
        "NT": "Green",
        "SA": "Blue",
    }

    assert is_consistent(assignment, "T", "Red") is True
    assert is_consistent(assignment, "T", "Green") is True
    assert is_consistent(assignment, "T", "Blue") is True


# ---------------------------------------------------------------------
# Test Case 3
# Category: unsolvable/over-constrained case.
# Connected triangles in the map cannot be coloured using only two colours.
# ---------------------------------------------------------------------
def test_case_3():
    from csp_map_coloring import VARIABLES

    solution = backtracking_search(VARIABLES, ["Red", "Green"])

    assert solution is None


if __name__ == "__main__":
    import sys

    sys.exit(pytest.main([__file__, "-v"]))
