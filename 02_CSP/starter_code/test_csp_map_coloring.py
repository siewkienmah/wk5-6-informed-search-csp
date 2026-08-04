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
from csp_map_coloring import backtracking_search, is_consistent


def _use_map(monkeypatch, variables, neighbours):
    """Helper: point the solver at a different constraint graph for one test.

    is_consistent() and select_unassigned_variable() read the module-level
    NEIGHBOURS and VARIABLES by design (the given function signatures don't
    pass them in), so a test that needs a different map has to swap those
    module attributes. monkeypatch restores them automatically afterwards,
    so tests stay independent of each other.
    """
    monkeypatch.setattr(csp, "VARIABLES", variables)
    monkeypatch.setattr(csp, "NEIGHBOURS", neighbours)


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
# Category: Solvability -> unsolvable (over-constrained), and
# "What You're Actually Checking" -> failure handling.
# Four mutually adjacent regions (K4) need 4 colours, so 3 colours cannot
# work. Chosen because the solver must exhaust the whole search tree and
# return None cleanly rather than crash, loop, or return a partial map.
# K4-with-3-colours is used rather than the triangle-with-2-colours from
# worked_example.md so this exercises a case not already hand-traced for us.
# ---------------------------------------------------------------------
def test_case_1(monkeypatch):
    variables = ["A", "B", "C", "D"]
    neighbours = {
        "A": ["B", "C", "D"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D"],
        "D": ["A", "B", "C"],
    }
    _use_map(monkeypatch, variables, neighbours)

    assert backtracking_search(variables, ["Red", "Green", "Blue"]) is None

    # Sanity check the same map IS solvable once a fourth colour is added,
    # proving the None above is genuine over-constraint, not a broken solver.
    solution = backtracking_search(variables, ["Red", "Green", "Blue", "Yellow"])
    assert _is_valid_solution(solution, variables, neighbours)


# ---------------------------------------------------------------------
# Test Case 2
# Category: Boundary Conditions -> single variable / minimal assignment,
# overlapping Input Size -> trivial smallest possible input.
# One unconstrained region with one available colour. Chosen because the
# smallest input is where off-by-one completeness checks and empty-loop
# handling break: the solver must return a complete assignment immediately
# without ever needing to backtrack.
# ---------------------------------------------------------------------
def test_case_2(monkeypatch):
    variables = ["Solo"]
    neighbours = {"Solo": []}
    _use_map(monkeypatch, variables, neighbours)

    # A region with no neighbours can never conflict, whatever is assigned.
    assert is_consistent({}, "Solo", "Red") is True

    solution = backtracking_search(variables, ["Red"])

    assert solution == {"Solo": "Red"}
    assert _is_valid_solution(solution, variables, neighbours)


# ---------------------------------------------------------------------
# Test Case 3
# Category: Structure of the Input -> symmetric graph, with Input Size ->
# larger than the given example, checking Validity.
# A 9-region ring (odd cycle). Every region looks identical to every other,
# so nothing about the structure hints at an answer, and an odd cycle
# provably needs a third colour only at the point where the ring closes --
# a good check that constraints are tested against ALL assigned neighbours
# (both ring partners), not just the most recently assigned one.
# ---------------------------------------------------------------------
def test_case_3(monkeypatch):
    n = 9
    variables = [f"R{i}" for i in range(n)]
    neighbours = {
        f"R{i}": [f"R{(i - 1) % n}", f"R{(i + 1) % n}"] for i in range(n)
    }
    _use_map(monkeypatch, variables, neighbours)

    solution = backtracking_search(variables, ["Red", "Green", "Blue"])

    assert _is_valid_solution(solution, variables, neighbours)
    # An odd cycle is not 2-colourable, so the same ring must fail on 2.
    assert backtracking_search(variables, ["Red", "Green"]) is None


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))
