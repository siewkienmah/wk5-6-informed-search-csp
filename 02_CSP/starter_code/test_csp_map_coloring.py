import pytest
from csp_map_coloring import backtracking_search, is_consistent, select_unassigned_variable, NEIGHBOURS

def test_case_1_three_colours_success():
    """
    Mind-map branch: Standard Valid Colouring (3 Colours)
    Tests that 3 colours (Red, Green, Blue) successfully produce a valid map assignment.
    """
    domain = ["Red", "Green", "Blue"]
    solution = backtracking_search({}, domain)
    
    assert solution is not None
    assert len(solution) == 7
    
    # Verify no adjacent regions share the same colour
    for var, value in solution.items():
        for neighbour in NEIGHBOURS[var]:
            assert solution[neighbour] != value


def test_case_2_two_colours_failure():
    """
    Mind-map branch: Insufficient Domain / Failure Case (2 Colours)
    Tests that 2 colours are insufficient to colour the mainland due to SA/NT/WA triangular loops.
    """
    domain = ["Red", "Green"]
    solution = backtracking_search({}, domain)
    
    assert solution is None


def test_case_3_isolated_region_tasmania():
    """
    Mind-map branch: Edge Case / Isolated Variable
    Tests that Tasmania (TAS) can be assigned any available colour independently of neighbours.
    """
    partial_assignment = {
        "WA": "Red",
        "NT": "Green",
        "SA": "Blue",
        "Q": "Red",
        "NSW": "Green",
        "V": "Red"
    }
    # TAS is unassigned
    var = select_unassigned_variable(partial_assignment)
    assert var == "TAS"
    
    # Check consistency for any colour since TAS has no neighbours
    assert is_consistent(partial_assignment, "TAS", "Red") is True
    assert is_consistent(partial_assignment, "TAS", "Green") is True