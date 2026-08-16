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
from csp_map_coloring import backtracking_search, is_consistent, NEIGHBOURS


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
# TODO Test Case 1
# Which mind-map category does this represent? (edit this comment)
# ---------------------------------------------------------------------
# ------------------------------------------------------------
# Test Case 1
# Category: Typical / solvable case.
# Tests a normal CSP with several connected regions and enough
# colours to produce a complete valid assignment.
# ------------------------------------------------------------
def test_case_1():
    variables = ["WA", "NT", "SA", "Q"]
    domain = ["Red", "Green", "Blue"]

    solution = backtracking_search(variables, domain)

    assert solution is not None
    assert set(solution.keys()) == set(variables)

    for var in variables:
        assert solution[var] in domain

    for var in variables:
        for neighbour in NEIGHBOURS[var]:
            if neighbour in solution:
                assert solution[var] != solution[neighbour]


# ------------------------------------------------------------
# Test Case 2
# Category: Boundary case.
# Tests the smallest CSP input: one variable with no neighbours.
# The solver should still assign a valid colour.
# ------------------------------------------------------------
def test_case_2():
    variables = ["T"]
    domain = ["Red", "Green", "Blue"]

    solution = backtracking_search(variables, domain)

    assert solution is not None
    assert set(solution.keys()) == set(variables)
    assert solution["T"] in domain


# ------------------------------------------------------------
# Test Case 3
# Category: Unsolvable / stress case.
# WA, NT and SA form a triangle where every pair is adjacent.
# With only two colours, no valid colouring can exist.
# ------------------------------------------------------------
def test_case_3():
    variables = ["WA", "NT", "SA"]
    domain = ["Red", "Green"]

    solution = backtracking_search(variables, domain)

    assert solution is None