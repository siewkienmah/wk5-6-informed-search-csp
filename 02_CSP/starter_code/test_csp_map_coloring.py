"""
Unit tests for csp_map_coloring.py.
"""
import pytest
from csp_map_coloring import (
    backtracking_search,
    is_consistent,
    VARIABLES,
    DOMAINS,
    NEIGHBORS,
)


def test_given_example():
    """Verify that the Australia map coloring solution is valid."""
    solution = backtracking_search(VARIABLES, DOMAINS, NEIGHBORS)
    assert solution is not None
    assert len(solution) == len(VARIABLES)
    for var, neighbors in NEIGHBORS.items():
        for n in neighbors:
            assert solution[var] != solution[n]


def test_case_1():
    """Category: Simple 2-node graph (Valid assignment)."""
    variables = ["A", "B"]
    domains = {"A": ["red", "blue"], "B": ["red", "blue"]}
    neighbors = {"A": ["B"], "B": ["A"]}

    solution = backtracking_search(variables, domains, neighbors)

    assert solution is not None
    assert solution["A"] != solution["B"]


def test_case_2():
    """Category: Impossible graph (Triangle with only 2 colors available)."""
    variables = ["A", "B", "C"]
    domains = {
        "A": ["red", "green"],
        "B": ["red", "green"],
        "C": ["red", "green"],
    }
    neighbors = {
        "A": ["B", "C"],
        "B": ["A", "C"],
        "C": ["A", "B"],
    }

    solution = backtracking_search(variables, domains, neighbors)

    assert solution is None


def test_case_3():
    """Category: Complete graph (Triangle with 3 colors available)."""
    variables = ["A", "B", "C"]
    domains = {
        "A": ["red", "green", "blue"],
        "B": ["red", "green", "blue"],
        "C": ["red", "green", "blue"],
    }
    neighbors = {
        "A": ["B", "C"],
        "B": ["A", "C"],
        "C": ["A", "B"],
    }

    solution = backtracking_search(variables, domains, neighbors)

    assert solution is not None
    assert len(set(solution.values())) == 3