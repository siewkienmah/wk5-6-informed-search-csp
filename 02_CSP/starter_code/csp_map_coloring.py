"""
Assignment starter: Map Coloring using CSP with Backtracking.

Read ../guide.md and ../worked_example.md BEFORE you start coding here.

Your job: fill in every function marked TODO. Do not change function
signatures (the tests rely on them).

run this file to verify that your implementation of the backtracking search algorithm is correct.
python 02_CSP/starter_code/csp_map_coloring.py
"""

# Map of Australia variables and neighbor relationships
AUSTRALIA_VARIABLES = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

AUSTRALIA_DOMAINS = {
    var: ["red", "green", "blue"] for var in AUSTRALIA_VARIABLES
}

AUSTRALIA_NEIGHBORS = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": [],  # Tasmania has no land borders
}

# Aliases expected by unit tests
VARIABLES = AUSTRALIA_VARIABLES
DOMAINS = AUSTRALIA_DOMAINS
NEIGHBORS = AUSTRALIA_NEIGHBORS


def is_consistent(var, color, assignment, neighbors):
    """Return True if assigning `color` to `var` does not conflict with neighbors.

    `assignment` is a dict mapping assigned variables to their chosen colors.
    `neighbors` is a dict mapping each variable to a list of adjacent variables.
    """
    for neighbor in neighbors.get(var, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def select_unassigned_variable(assignment, variables):
    """Return the next unassigned variable from `variables`.

    Returns the first variable in `variables` that is not yet in `assignment`.
    """
    for var in variables:
        if var not in assignment:
            return var
    return None


def backtracking_search(variables, domains, neighbors, assignment=None):
    """Implement Backtracking Search for Map Coloring CSP.

    Return a dict mapping variable -> color if a valid assignment exists,
    or None if no solution exists.
    """
    if assignment is None:
        assignment = {}

    # Base case: if all variables are assigned, return the complete assignment
    if len(assignment) == len(variables):
        return assignment

    var = select_unassigned_variable(assignment, variables)

    for value in domains[var]:
        if is_consistent(var, value, assignment, neighbors):
            assignment[var] = value
            result = backtracking_search(variables, domains, neighbors, assignment)
            if result is not None:
                return result
            # Backtrack
            del assignment[var]

    return None


if __name__ == "__main__":
    solution = backtracking_search(
        AUSTRALIA_VARIABLES, AUSTRALIA_DOMAINS, AUSTRALIA_NEIGHBORS
    )
    if solution:
        print("Solution found:")
        for var, color in solution.items():
            print(f"  {var}: {color}")
    else:
        print("No solution found.")