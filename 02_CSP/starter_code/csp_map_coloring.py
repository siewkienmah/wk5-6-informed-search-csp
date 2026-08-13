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
    """Return True if assigning `value` to `var` does not conflict
    with any already-assigned neighbour of `var`.

    `assignment` is a dict {variable: value} of variables assigned so far.
    Use NEIGHBOURS[var] to find which variables to check against.
    """
    for neighbour in NEIGHBOURS.get(var, []):
        if neighbour in assignment and assignment[neighbour] == value:
            return False
    return True


def select_unassigned_variable(assignment):
    """Return the name of a variable from VARIABLES that is not yet
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
    """Run backtracking search and return a complete, consistent
    assignment (dict {variable: value}), or None if no solution exists.

    Follow the pseudocode in ../guide.md section 2:
      1. If the assignment is complete, return it.
      2. Otherwise pick an unassigned variable (select_unassigned_variable).
      3. Try each value in `domain` for that variable, in order.
      4. If is_consistent(), tentatively assign it and recurse.
      5. If the recursive call succeeds, return its result.
      6. If it fails, undo the assignment (backtrack) and try the next
         value.
      7. If no value works, return None (failure) so the caller backtracks
         further.

    Tip: write a helper function backtrack(assignment) and call it with
    an empty dict to start.
    """
    solution, _ = _backtracking_search_with_count(variables, domain)
    return solution


def _backtracking_search_with_count(variables, domain):
    """Run plain backtracking and also count recursive states explored."""
    nodes_explored = 0

    def backtrack(assignment):
        nonlocal nodes_explored
        nodes_explored += 1

        if len(assignment) == len(variables):
            return assignment.copy()

        var = select_unassigned_variable(assignment)
        if var is None or var not in variables:
            var = next((v for v in variables if v not in assignment), None)
        if var is None:
            return None

        for value in domain:
            if is_consistent(assignment, var, value):
                assignment[var] = value
                result = backtrack(assignment)
                if result is not None:
                    return result
                del assignment[var]

        return None

    return backtrack({}), nodes_explored


def backtracking_search_with_count(variables, domain):
    """Bonus helper returning ``(solution, recursive_states_explored)``."""
    return _backtracking_search_with_count(variables, domain)


def forward_checking_search(variables, domain, return_node_count=False):
    """Solve the CSP using forward checking.

    After each assignment, the chosen colour is removed from every
    unassigned neighbour's remaining domain. A branch is pruned immediately
    if that leaves any domain empty. Set `return_node_count` to True to also
    receive the number of recursive states explored.
    """
    nodes_explored = 0
    initial_domains = {variable: list(domain) for variable in variables}

    def backtrack(assignment, remaining_domains):
        nonlocal nodes_explored
        nodes_explored += 1

        if len(assignment) == len(variables):
            return assignment.copy()

        var = select_unassigned_variable(assignment)
        if var is None or var not in variables:
            var = next((v for v in variables if v not in assignment), None)
        if var is None:
            return None

        for value in remaining_domains[var]:
            if not is_consistent(assignment, var, value):
                continue

            assignment[var] = value
            next_domains = {
                variable: list(values)
                for variable, values in remaining_domains.items()
            }
            domains_remain = True

            for neighbour in NEIGHBOURS.get(var, []):
                if neighbour in assignment or neighbour not in next_domains:
                    continue
                if value in next_domains[neighbour]:
                    next_domains[neighbour].remove(value)
                if not next_domains[neighbour]:
                    domains_remain = False
                    break

            if domains_remain:
                result = backtrack(assignment, next_domains)
                if result is not None:
                    return result

            del assignment[var]

        return None

    solution = backtrack({}, initial_domains)
    if return_node_count:
        return solution, nodes_explored
    return solution


if __name__ == "__main__":
    solution = backtracking_search(VARIABLES, DOMAIN)
    if solution:
        print("Solution found:")
        for region in VARIABLES:
            print(f"  {region}: {solution[region]}")
    else:
        print("No solution exists with this domain.")
