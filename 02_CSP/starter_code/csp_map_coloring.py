"""
Assignment starter: backtracking CSP solver for map colouring.

Read ../guide.md and ../worked_example.md BEFORE you start coding here.

Your job: fill in every function marked TODO. Do not change function
signatures (the tests in test_csp_map_coloring.py rely on them).

The problem: colour a map of Australia's 7 regions so that no two adjacent
regions share a colour, using only 3 colours.
"""

VARIABLES = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

# Adjacency list: which regions border which. T (Tasmania) is an island --
# it has no neighbours, so it's unconstrained.
NEIGHBOURS = {
    "WA":  ["NT", "SA"],
    "NT":  ["WA", "SA", "Q"],
    "SA":  ["WA", "NT", "Q", "NSW", "V"],
    "Q":   ["NT", "SA", "NSW"],
    "NSW": ["SA", "Q", "V"],
    "V":   ["SA", "NSW"],
    "T":   [],
}

DOMAIN = ["Red", "Green", "Blue"]


def is_consistent(assignment, var, value):
    """Return True if value does not conflict with assigned neighbours."""
    for neighbour in NEIGHBOURS[var]:
        if neighbour in assignment and assignment[neighbour] == value:
            return False

    return True


def select_unassigned_variable(assignment):
    """Return the first unassigned variable, or None if complete."""
    for variable in VARIABLES:
        if variable not in assignment:
            return variable

    return None


def backtracking_search(variables, domain):
    """Return a complete consistent assignment, or None if unsolvable."""

    def backtrack(assignment):
        # Success: every requested variable has been assigned.
        if all(variable in assignment for variable in variables):
            return assignment.copy()

        var = select_unassigned_variable(assignment)

        if var is None:
            return assignment.copy()

        for value in domain:
            if is_consistent(assignment, var, value):
                assignment[var] = value

                result = backtrack(assignment)
                if result is not None:
                    return result

                # Undo the tentative assignment.
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