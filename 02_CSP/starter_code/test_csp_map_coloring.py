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
# Mind-map category: Solvability -> Over-constrained / Unsolvable Case
# Why: Tests solver behavior when insufficient domain values are provided.
# The mainland Australia map contains mutually adjacent triangles (e.g., SA-WA-NT)
# that require at least 3 colors. Restricting domain to 2 colors must return None.
# ---------------------------------------------------------------------
def test_case_1():
    from csp_map_coloring import VARIABLES

    two_color_domain = ["Red", "Green"]
    solution = backtracking_search(VARIABLES, two_color_domain)

    assert solution is None


# ---------------------------------------------------------------------
# Test Case 2
# Mind-map category: Constraint Checking -> Direct Neighbor Conflict Detection
# Why: Directly tests `is_consistent()` logic to verify that assigning a color
# already held by an adjacent neighbor returns False, while assigning a distinct
# color returns True.
# ---------------------------------------------------------------------
def test_case_2():
    # WA and NT are adjacent neighbors in NEIGHBOURS
    partial_assignment = {"WA": "Red"}

    # Assigning 'Red' to NT should conflict with WA
    assert is_consistent(partial_assignment, "NT", "Red") is False

    # Assigning 'Blue' to NT should be consistent with WA
    assert is_consistent(partial_assignment, "NT", "Blue") is True


# ---------------------------------------------------------------------
# Test Case 3
# Mind-map category: Graph Structure -> Hub Variable / High Degree Constraints
# Why: Tests constraint satisfaction around "SA" (South Australia), which is the
# highest-degree node bordering 5 other regions. Ensures none of its 5 neighbors
# share its assigned color in a complete solution.
# ---------------------------------------------------------------------
def test_case_3():
    from csp_map_coloring import VARIABLES, NEIGHBOURS, DOMAIN

    solution = backtracking_search(VARIABLES, DOMAIN)
    assert solution is not None

    sa_color = solution["SA"]
    for neighbor in NEIGHBOURS["SA"]:
        assert solution[neighbor] != sa_color


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))