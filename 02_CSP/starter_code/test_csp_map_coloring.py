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
import csp_map_coloring
from csp_map_coloring import (
    backtracking_search,
    backtracking_search_with_count,
    forward_checking_search,
    is_consistent,
)


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
# Category: Boundary Conditions -> single variable, the smallest complete CSP.
# ---------------------------------------------------------------------
def test_case_1(monkeypatch):
    variables = ["A"]
    neighbours = {"A": []}
    monkeypatch.setattr(csp_map_coloring, "VARIABLES", variables)
    monkeypatch.setattr(csp_map_coloring, "NEIGHBOURS", neighbours)

    solution = backtracking_search(variables, ["Red"])

    assert _is_valid_solution(solution, variables, neighbours)


# ---------------------------------------------------------------------
# Test Case 2
# Category: Correctness -> validity, checking every already-assigned neighbour.
# ---------------------------------------------------------------------
def test_case_2():
    assignment = {"WA": "Red", "NT": "Green"}

    assert not is_consistent(assignment, "SA", "Red")
    assert not is_consistent(assignment, "SA", "Green")
    assert is_consistent(assignment, "SA", "Blue")


# ---------------------------------------------------------------------
# Test Case 3
# Category: Solvability -> unsolvable, a triangle cannot use only two colours.
# ---------------------------------------------------------------------
def test_case_3(monkeypatch):
    variables = ["A", "B", "C"]
    neighbours = {
        "A": ["B", "C"],
        "B": ["A", "C"],
        "C": ["A", "B"],
    }
    monkeypatch.setattr(csp_map_coloring, "VARIABLES", variables)
    monkeypatch.setattr(csp_map_coloring, "NEIGHBOURS", neighbours)

    solution = backtracking_search(variables, ["Red", "Green"])

    assert solution is None


def test_searches_honour_variables_argument():
    """Custom variables are assigned even when absent from the map globals."""
    variables = ["A", "B"]
    domain = ["Red", "Green"]

    plain_solution = backtracking_search(variables, domain)
    forward_solution = forward_checking_search(variables, domain)

    assert plain_solution == {"A": "Red", "B": "Red"}
    assert forward_solution == {"A": "Red", "B": "Red"}


def test_forward_checking_bonus(monkeypatch):
    """Forward checking prunes the two-colour triangle earlier."""
    variables = ["A", "B", "C"]
    neighbours = {
        "A": ["B", "C"],
        "B": ["A", "C"],
        "C": ["A", "B"],
    }
    domain = ["Red", "Green"]
    monkeypatch.setattr(csp_map_coloring, "VARIABLES", variables)
    monkeypatch.setattr(csp_map_coloring, "NEIGHBOURS", neighbours)

    plain_solution, plain_nodes = backtracking_search_with_count(
        variables, domain
    )
    forward_solution, forward_nodes = forward_checking_search(
        variables, domain, return_node_count=True
    )

    assert plain_solution is None
    assert forward_solution is None
    assert plain_nodes == 5
    assert forward_nodes == 3
    assert forward_nodes < plain_nodes


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))
