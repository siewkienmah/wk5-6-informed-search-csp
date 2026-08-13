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
# Category: Boundary Conditions -> a variable with no constraints at
# all (Structure -> isolated node). Tasmania (T) has NEIGHBOURS["T"] ==
# [], so it should be consistent with *every* colour regardless of how
# the rest of the map is assigned. This checks is_consistent() doesn't
# accidentally reject an unconstrained variable, a common off-by-one
# trap when looping over an empty neighbour list.
# ---------------------------------------------------------------------
def test_case_1_isolated_variable_has_no_constraints():
    from csp_map_coloring import DOMAIN

    assignment = {
        "WA": "Red", "NT": "Green", "SA": "Blue",
        "Q": "Red", "NSW": "Green", "V": "Red",
    }
    for colour in DOMAIN:
        assert is_consistent(assignment, "T", colour) is True


# ---------------------------------------------------------------------
# Test Case 2
# Category: What You're Actually Checking -> Validity (constraint-
# violation detection), tested directly on is_consistent() rather than
# through the full search. WA and NT are adjacent, so assigning NT the
# same colour as an already-assigned WA must be rejected, while a
# different colour must be accepted. This isolates the constraint-
# checking logic from the search/backtracking logic.
# ---------------------------------------------------------------------
def test_case_2_conflict_with_assigned_neighbour_detected():
    assignment = {"WA": "Red"}

    assert is_consistent(assignment, "NT", "Red") is False  # WA-NT adjacent
    assert is_consistent(assignment, "NT", "Green") is True  # no conflict


# ---------------------------------------------------------------------
# Test Case 3
# Category: Solvability -> unsolvable / over-constrained (Structure ->
# dense constraint graph). WA, NT and SA are mutually adjacent (a
# triangle), so -- exactly like the 2-colour triangle in
# worked_example.md -- the real Australia map cannot be coloured with
# only 2 colours. This checks backtracking_search() explores every
# branch and correctly reports failure (None) instead of crashing or
# looping forever, on the full-size problem rather than the toy one.
# ---------------------------------------------------------------------
def test_case_3_two_colours_unsolvable():
    from csp_map_coloring import VARIABLES

    solution = backtracking_search(VARIABLES, ["Red", "Green"])

    assert solution is None


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))
