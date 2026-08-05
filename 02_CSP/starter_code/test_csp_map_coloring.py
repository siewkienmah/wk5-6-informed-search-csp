"""
Tests for csp_map_coloring.py

Run with:
    pytest 02_CSP/starter_code/test_csp_map_coloring.py -v
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
    from csp_map_coloring import VARIABLES, NEIGHBOURS, DOMAIN

    solution = backtracking_search(VARIABLES, DOMAIN)

    assert solution is not None
    assert _is_valid_solution(solution, VARIABLES, NEIGHBOURS)


# ---------------------------------------------------------------------
# TEST CASE 1 - Solvable case with 3 colors
# Category: Solvability -> solvable case
# Why: Tests that Australia map can be colored with 3 colors
# ---------------------------------------------------------------------
def test_case_1():
    from csp_map_coloring import VARIABLES, NEIGHBOURS, DOMAIN

    solution = backtracking_search(VARIABLES, DOMAIN)

    # Should find a solution
    assert solution is not None
    assert _is_valid_solution(solution, VARIABLES, NEIGHBOURS)
    
    # All 7 regions should be assigned
    assert len(solution) == len(VARIABLES)


# ---------------------------------------------------------------------
# TEST CASE 2 - Unsolvable case with 2 colors
# Category: Unsolvable -> over-constrained
# Why: Australia map needs 3 colors, so 2 colors should fail
# ---------------------------------------------------------------------
def test_case_2():
    from csp_map_coloring import VARIABLES, NEIGHBOURS

    # Try with only 2 colors (Red and Green)
    domain_2 = ["Red", "Green"]
    solution = backtracking_search(VARIABLES, domain_2)

    # Should fail (no solution with only 2 colors)
    assert solution is None


# ---------------------------------------------------------------------
# TEST CASE 3 - Verify no two neighbors share same color
# Category: Constraint checking -> consistency
# Why: Tests that the solution satisfies all constraints
# ---------------------------------------------------------------------
def test_case_3():
    from csp_map_coloring import VARIABLES, NEIGHBOURS, DOMAIN

    solution = backtracking_search(VARIABLES, DOMAIN)

    # Solution must exist
    assert solution is not None

    # Check every constraint: no two adjacent regions share a color
    for region, neighbors in NEIGHBOURS.items():
        for neighbor in neighbors:
            assert solution[region] != solution[neighbor]
    
    # Check that all regions are in the solution
    for region in VARIABLES:
        assert region in solution


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))