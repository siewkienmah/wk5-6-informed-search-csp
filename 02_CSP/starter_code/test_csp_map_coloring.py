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
import csp_map_coloring as csp


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
    # backtracking_search() in this starter file solves the fixed Australia
    # map problem using the module-level VARIABLES / NEIGHBOURS / DOMAIN.
    solution = csp.backtracking_search(csp.VARIABLES, csp.DOMAIN)

    assert solution is not None
    assert _is_valid_solution(solution, csp.VARIABLES, csp.NEIGHBOURS)


# ---------------------------------------------------------------------
# TODO Test Case 1
# Which mind-map category does this represent? (edit this comment)
# ---------------------------------------------------------------------
def test_case_1(monkeypatch):
    # Category: Structure -> simple, solvable case. A small chain checks
    # that adjacent regions receive different colours.
    monkeypatch.setattr(csp, "VARIABLES", ["A", "B", "C"])
    monkeypatch.setattr(csp, "NEIGHBOURS", {
        "A": ["B"],
        "B": ["A", "C"],
        "C": ["B"],
    })

    solution = csp.backtracking_search(csp.VARIABLES, ["Red", "Green"])

    assert solution is not None
    assert _is_valid_solution(solution, csp.VARIABLES, csp.NEIGHBOURS)


# ---------------------------------------------------------------------
# TODO Test Case 2
# Which mind-map category does this represent? (edit this comment)
# ---------------------------------------------------------------------
def test_case_2(monkeypatch):
    # Category: Boundary -> single variable. This checks the smallest CSP
    # where one variable can be assigned without any constraints.
    monkeypatch.setattr(csp, "VARIABLES", ["A"])
    monkeypatch.setattr(csp, "NEIGHBOURS", {"A": []})

    solution = csp.backtracking_search(csp.VARIABLES, ["Red", "Green"])

    assert solution == {"A": "Red"}


# ---------------------------------------------------------------------
# TODO Test Case 3
# Which mind-map category does this represent? (edit this comment)
# ---------------------------------------------------------------------
def test_case_3(monkeypatch):
    # Category: Solvability -> unsolvable. A triangle needs three colours,
    # so two colours must cause the backtracking solver to return failure.
    monkeypatch.setattr(csp, "VARIABLES", ["A", "B", "C"])
    monkeypatch.setattr(csp, "NEIGHBOURS", {
        "A": ["B", "C"],
        "B": ["A", "C"],
        "C": ["A", "B"],
    })

    solution = csp.backtracking_search(csp.VARIABLES, ["Red", "Green"])

    assert solution is None


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))
