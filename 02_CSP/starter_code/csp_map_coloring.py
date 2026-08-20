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
    """TODO: return True if assigning `value` to `var` does not conflict
    with any already-assigned neighbour of `var`.

    `assignment` is a dict {variable: value} of variables assigned so far.
    Use NEIGHBOURS[var] to find which variables to check against.
    """
    for neighbour in NEIGHBOURS[var]:
        if neighbour in assignment and assignment[neighbour] == value:
            return False

    return True


def select_unassigned_variable(assignment):
    """TODO: return the name of a variable from VARIABLES that is not yet
    a key in `assignment`. Return None if all variables are assigned.

    A simple valid strategy: return the first unassigned variable in
    VARIABLES order. (Bonus/optional: implement the MRV heuristic instead
    -- see ../guide.md section 3.)
    """
    for variable in VARIABLES:
        if variable not in assignment:
            return variable

    return None


def backtracking_search(variables, domain):
    def backtrack(assignment):
        # If all variables are assigned, return the solution
        if len(assignment) == len(variables):
            return assignment.copy()

        # Pick an unassigned variable
        var = select_unassigned_variable(assignment)

        # Try each value in the domain
        for value in domain:
            # Check whether this value is consistent
            if is_consistent(assignment, var, value):
                assignment[var] = value

                # Recursively search for a solution
                result = backtrack(assignment)

                # If a solution was found, return it
                if result is not None:
                    return result

                # Otherwise, undo the assignment
                del assignment[var]

        # No value worked
        return None

    # Start with an empty assignment
    return backtrack({})


if __name__ == "__main__":
    solution = backtracking_search(VARIABLES, DOMAIN)
    if solution:
        print("Solution found:")
        for region in VARIABLES:
            print(f"  {region}: {solution[region]}")
    else:
        print("No solution exists with this domain.")
