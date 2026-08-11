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
# TODO Test Case 1
# Which mind-map category does this represent? (edit this comment)
# ---------------------------------------------------------------------
def test_case_1():
    # Category: Validity / solvable case.
    # Checks that a normal Australia map solution satisfies all constraints.
    from csp_map_coloring import VARIABLES, NEIGHBOURS, DOMAIN

    solution = backtracking_search(VARIABLES, DOMAIN)

    assert solution is not None
    assert _is_valid_solution(solution, VARIABLES, NEIGHBOURS)

# ---------------------------------------------------------------------
# TODO Test Case 2
# Which mind-map category does this represent? (edit this comment)
# ---------------------------------------------------------------------
def test_case_2():
    # Category: Boundary condition.
    # Tasmania has no neighbours, so any colour should be consistent.
    assignment = {}

    assert is_consistent(assignment, "T", "Red") is True
    assert is_consistent(assignment, "T", "Green") is True
    assert is_consistent(assignment, "T", "Blue") is True

# ---------------------------------------------------------------------
# TODO Test Case 3
# Which mind-map category does this represent? (edit this comment)
# ---------------------------------------------------------------------
def test_case_3():
    # Category: Failure handling / conflicting assignment.
    # WA and NT are neighbours, so they cannot use the same colour.
    assignment = {"WA": "Red"}

    assert is_consistent(assignment, "NT", "Red") is False
    assert is_consistent(assignment, "NT", "Green") is True

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))
