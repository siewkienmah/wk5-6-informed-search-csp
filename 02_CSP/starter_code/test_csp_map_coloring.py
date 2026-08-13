"""
Tests for csp_map_coloring.py
...
"""
import pytest
from csp_map_coloring import backtracking_search, is_consistent


def _is_valid_solution(solution, variables, neighbours):
    ...


# GIVEN EXAMPLE (unchanged)
def test_given_example():
    ...


# ---------------------------------------------------------------------
# Test Case 1
# Category: edge / boundary case — unconstrained variable (Tasmania has
# no neighbours). Chosen to verify that a variable with an empty neighbour
# list is always consistent with any colour and does not block search.
# ---------------------------------------------------------------------
def test_case_1():
    empty_assignment = {}
    assert is_consistent(empty_assignment, "T", "Red") is True
    assert is_consistent(empty_assignment, "T", "Green") is True
    assert is_consistent(empty_assignment, "T", "Blue") is True

    partial = {"WA": "Red", "NT": "Green", "SA": "Blue"}
    assert is_consistent(partial, "T", "Red") is True
    assert is_consistent(partial, "T", "Green") is True
    assert is_consistent(partial, "T", "Blue") is True


# ---------------------------------------------------------------------
# Test Case 2
# Category: constraint-checking / conflict detection (negative partial
# assignment). Chosen because a correct is_consistent() must reject a
# colour that clashes with an already-assigned neighbour, and accept a
# colour that does not.
# ---------------------------------------------------------------------
def test_case_2():
    partial = {"WA": "Red"}
    assert is_consistent(partial, "NT", "Red") is False
    assert is_consistent(partial, "NT", "Green") is True
    assert is_consistent(partial, "NT", "Blue") is True

    partial2 = {"WA": "Red", "NT": "Green"}
    assert is_consistent(partial2, "SA", "Red") is False
    assert is_consistent(partial2, "SA", "Green") is False
    assert is_consistent(partial2, "SA", "Blue") is True


# ---------------------------------------------------------------------
# Test Case 3
# Category: unsolvable / over-constrained case (domain too small).
# Chosen to verify that backtracking_search correctly returns None when
# no complete consistent assignment exists. We temporarily shrink the
# domain to a single colour, which makes the Australia map uncolourable.
# ---------------------------------------------------------------------
def test_case_3():
    from csp_map_coloring import VARIABLES, NEIGHBOURS

    tiny_domain = ["Red"]
    solution = backtracking_search(VARIABLES, tiny_domain)

    assert solution is None