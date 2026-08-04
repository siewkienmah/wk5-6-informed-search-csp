"""
CSP Map Colouring — Australia Map

Variables represent states/territories.
Domains represent available colours.
Constraints specify that adjacent regions cannot share the same colour.
"""

# Variables (Regions of Australia)
VARIABLES = ["WA", "NT", "SA", "Q", "NSW", "V", "TAS"]

# Adjacency Graph Constraints
NEIGHBOURS = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "TAS": []  # Tasmania shares no land borders
}


def is_consistent(assignment: dict[str, str], var: str, value: str) -> bool:
    """
    Checks if assigning `value` to `var` violates any constraints with already assigned neighbours.
    """
    for neighbour in NEIGHBOURS[var]:
        if neighbour in assignment and assignment[neighbour] == value:
            return False
    return True


def select_unassigned_variable(assignment: dict[str, str]) -> str | None:
    """
    Selects the next variable to assign using standard order (first unassigned variable in VARIABLES).
    """
    for var in VARIABLES:
        if var not in assignment:
            return var
    return None


def backtracking_search(assignment: dict[str, str], domain: list[str]) -> dict[str, str] | None:
    """
    Executes standard Backtracking Search to find a valid map colouring.
    Returns: Complete assignment dict if successful, or None if no valid colouring exists.
    """
    if len(assignment) == len(VARIABLES):
        return dict(assignment)

    var = select_unassigned_variable(assignment)
    if var is None:
        return None

    for value in domain:
        if is_consistent(assignment, var, value):
            assignment[var] = value
            result = backtracking_search(assignment, domain)
            if result is not None:
                return result
            del assignment[var]  

    return None