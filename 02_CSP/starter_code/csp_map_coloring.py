"""
Assignment starter: backtracking CSP solver for map colouring.

Read ../guide.md and ../worked_example.md BEFORE you start coding here.

Your job: fill in every function marked TODO. Do not change function
signatures (the tests in test_csp_map_coloring.py rely on them).

The problem: colour a map of Australia's 7 regions so that no two adjacent
regions share a colour, using only 3 colours.
"""

VARIABLES = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

NEIGHBOURS = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["SA", "Q", "V"],
    "V": ["SA", "NSW"],
    "T": [],
}

DOMAIN = ["Red", "Green", "Blue"]


def is_consistent(assignment, var, value):
    """Return True if assigning `value` to `var` is consistent with `assignment`."""
    for neighbor in NEIGHBOURS.get(var, []):
        if neighbor in assignment and assignment[neighbor] == value:
            return False
    return True


def select_unassigned_variable(assignment, variables=VARIABLES):
    """Return the first unassigned variable from `variables`."""
    for var in variables:
        if var not in assignment:
            return var
    return None


def backtracking_search(variables=VARIABLES, domain=DOMAIN):
    """Solve the CSP using recursive backtracking search."""

    def backtrack(assignment):
        if len(assignment) == len(variables):
            return assignment

        var = select_unassigned_variable(assignment, variables)

        for value in domain:
            if is_consistent(assignment, var, value):
                assignment[var] = value

                result = backtrack(assignment)
                if result is not None:
                    return result

                # Backtrack
                del assignment[var]

        return None

    return backtrack({})


if __name__ == "__main__":
    solution = backtracking_search(VARIABLES, DOMAIN)
    if solution:
        print("Solution found:")
        for region in VARIABLES:
            print(f"  {region}: {solution[region]}")
    else:
        print("No solution exists with this domain.")