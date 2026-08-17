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
# Category: Solvability -> Unsolvable / Over-constrained case
# Why: Tests that the algorithm returns None when given fewer colors than
# required (2 colors for a graph containing 3-cliques like WA-NT-SA).
# ---------------------------------------------------------------------
def test_case_1():
    from csp_map_coloring import VARIABLES
    two_color_domain = ["Red", "Green"]

    solution = backtracking_search(VARIABLES, two_color_domain)

    assert solution is None


# ---------------------------------------------------------------------
# Test Case 2
# Category: Boundary / Edge Cases -> Trivial / Single isolated region
# Why: Tests boundary execution with a single unconstrained region ("T")
# and a minimal domain of size 1 to ensure simple edge cases pass cleanly.
# ---------------------------------------------------------------------
def test_case_2():
    from csp_map_coloring import NEIGHBOURS
    single_var = ["T"]
    single_domain = ["Blue"]

    solution = backtracking_search(single_var, single_domain)

    assert solution is not None
    assert solution == {"T": "Blue"}
    assert _is_valid_solution(solution, single_var, NEIGHBOURS)


# ---------------------------------------------------------------------
# Test Case 3
# Category: Structure -> Subgraph / Partial map constraint
# Why: Tests solver correctness on a smaller 3-region fully connected
# sub-map (WA, NT, SA) to verify backtracking on tighter sub-problems.
# ---------------------------------------------------------------------
def test_case_3():
    from csp_map_coloring import NEIGHBOURS, DOMAIN
    sub_vars = ["WA", "NT", "SA"]

    solution = backtracking_search(sub_vars, DOMAIN)

    assert solution is not None
    assert _is_valid_solution(solution, sub_vars, NEIGHBOURS)


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))