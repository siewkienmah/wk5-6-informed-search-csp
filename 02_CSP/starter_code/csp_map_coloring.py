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
    """Return True if assigning `value` to `var` does not conflict with any
    already-assigned neighbour of `var`.

    `assignment` is a dict {variable: value} of variables assigned so far.
    Every neighbour in NEIGHBOURS[var] is checked, not just the most
    recently assigned one. Neighbours that are still unassigned cannot
    conflict yet, so .get() returning None is treated as "no conflict"
    (None is never a legal colour).
    """
    return all(assignment.get(neighbour) != value for neighbour in NEIGHBOURS[var])


def select_unassigned_variable(assignment):
    """Return the first variable in VARIABLES order that is not yet a key in
    `assignment`, or None if all variables are assigned.

    This is the simple "first unassigned" strategy. MRV would pick the
    variable with the fewest remaining legal values instead; plain
    backtracking is the baseline requirement here, so ordering is kept
    deterministic and easy to hand-trace against ../worked_example.md.
    """
    return next((var for var in VARIABLES if var not in assignment), None)


def backtracking_search(variables, domain):
    """Run backtracking search over `variables` using value set `domain`.

    Returns a complete, consistent assignment (dict {variable: value}), or
    None if no solution exists. Follows the pseudocode in ../guide.md
    section 2: pick an unassigned variable, try each domain value that is
    consistent with the partial assignment, recurse, and undo the
    assignment on failure so the caller can try its next value.

    Note: `variables` supplies the completeness test, while the constraint
    graph is read from the module-level NEIGHBOURS, and the variable order
    from module-level VARIABLES (both fixed by the given function
    signatures). Callers must therefore pass the same list that VARIABLES
    holds -- the tests swap all of them together for each map.
    """

    def backtrack(assignment):
        if len(assignment) == len(variables):
            return dict(assignment)

        var = select_unassigned_variable(assignment)
        for value in domain:
            if is_consistent(assignment, var, value):
                assignment[var] = value
                result = backtrack(assignment)
                if result is not None:
                    return result
                del assignment[var]  # backtrack: undo before the next value

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
