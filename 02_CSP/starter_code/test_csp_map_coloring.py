"""
Tests for csp_map_coloring.py

Run with:
    pytest 02_CSP/starter_code/test_csp_map_coloring.py -v

`test_given_example` below is COMPLETE -- study it as a template.

You must then write the 3 required test cases (test_case_1, test_case_2,
test_case_3). Read ../../03_Test_Case_Design/mindmap.md and
training_guide.md before choosing what your 3 cases should cover. Aim to
pick 3 *different* categories rather than 3 variations of the same thing
(e.g. one typical/solvable case, one edge/boundary case, one
unsolvable/over-constrained case).

For each test case, write a short comment explaining WHICH category from
the mind-map it represents and WHY you chose it.
"""
import pytest
from csp_map_coloring import backtracking_search, is_consistent


def _is_valid_solution(solution, variables, neighbours):
    """Helper: check a solution assigns every variable and breaks no
    adjacency constraint. Already implemented -- reuse this in your tests.
    """
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
# GIVEN EXAMPLE -- complete, do not modify. Use this as your template.
# Category: typical/normal small solvable case (from the mind-map:
# "Solvability -> solvable case").
# ---------------------------------------------------------------------
def test_given_example():
    # backtracking_search() in this starter file is wired to the fixed
    # Australia map problem (VARIABLES / NEIGHBOURS / DOMAIN, all module
    # level in csp_map_coloring.py), so this test solves that real problem.
    from csp_map_coloring import VARIABLES, NEIGHBOURS, DOMAIN

    solution = backtracking_search(VARIABLES, DOMAIN)

    assert solution is not None
    assert _is_valid_solution(solution, VARIABLES, NEIGHBOURS)


# ---------------------------------------------------------------------
# Test Case 1
# Category: Constraint checking -> conflicting adjacent regions.
# Why I chose it: This directly tests that is_consistent() rejects assigning
# the same colour to two neighbouring regions.
# ---------------------------------------------------------------------
def test_case_1():
    assignment = {
        "NT": "Red"
    }

    # WA and NT are neighbours, so WA cannot also be Red.
    assert is_consistent(assignment, "WA", "Red") is False

    # A different colour should be allowed.
    assert is_consistent(assignment, "WA", "Green") is True


# ---------------------------------------------------------------------
# Test Case 2
# Category: Edge/boundary case -> isolated unconstrained variable.
# Why I chose it: Tasmania has no neighbours, so any colour should remain
# consistent regardless of the colours assigned to other regions.
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
# Category: Solvability -> unsolvable/over-constrained case.
# Why I chose it: WA, NT, and SA form a triangle, so they require three
# different colours. A domain containing only two colours cannot solve
# the Australia map.
# ---------------------------------------------------------------------
def test_case_3():
    from csp_map_coloring import VARIABLES

    two_colour_domain = ["Red", "Green"]

    solution = backtracking_search(VARIABLES, two_colour_domain)

    assert solution is None
    
if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))