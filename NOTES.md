# NOTES.md — Informed Search (A*) & CSP Map Colouring

This file records the key design decisions, correctness arguments, and test-case rationale for the two assignments.

---

## 1. A* Search on a Grid

### 1.1 Why Manhattan distance is an admissible heuristic

For 4-directional grid movement the true cost of a path is exactly the number of orthogonal steps taken.  
The Manhattan distance never over-estimates that cost: you cannot reach the goal in fewer steps than the sum of the absolute differences in each coordinate.  
Because `h(n) ≤ h*(n)` for every node `n`, the heuristic is **admissible**.  
A* with an admissible heuristic is guaranteed to return an optimal path (when one exists).

It is also **consistent** (the triangle inequality holds for grid steps of cost 1), so the first time the goal is dequeued it is already optimally solved; we therefore stop as soon as the goal is popped from the open list.

### 1.2 Implementation notes

- **Open list** – a binary heap of tuples `(f, −g, row, col, node)`.  
  The secondary key `−g` gives a deterministic tie-break that prefers nodes with larger `g` (more progress toward the goal).
- **Closed set** – nodes that have already been expanded are never re-expanded.
- **Early termination** – we only return a solution when the goal is *popped*, not when it is first generated as a neighbour. This is required for optimality with a consistent heuristic.
- **Path reconstruction** – the `came_from` map is walked backwards from the goal to the start and then reversed.

### 1.3 Test-case design (A*)

| Test                 | Mind-map category              | Why it was chosen                                                                             |
|----------------------|--------------------------------|-----------------------------------------------------------------------------------------------|
| `test_given_example` | Typical / no obstacles         | Baseline “happy path” supplied by the starter.                                                |
| `test_case_1`        | Typical with obstacles         | Forces the search to route around walls and still return a shortest path.                     |
| `test_case_2`        | Edge / boundary                | Covers the two extreme distances: start == goal (cost 0) and start adjacent to goal (cost 1). |
| `test_case_3`        | Unsolvable / no-path           | Verifies that an empty open list correctly yields `(None, ∞)`.                                |

These three categories are deliberately distinct: one ordinary solvable instance with obstacles, one minimal-distance edge case, and one negative (impossible) instance.

---

## 2. CSP Map Colouring (Australia)

### 2.1 Backtracking search

The solver follows the classic recursive formulation:

1. If every variable is assigned → return the assignment (success).
2. Select an unassigned variable (simple left-to-right order).
3. For each value in the domain:
   - if the value is consistent with already-assigned neighbours, assign it and recurse;
   - if the recursive call succeeds, propagate the solution upward;
   - otherwise undo the assignment (backtrack) and try the next value.
4. If no value works → return `None` (failure).

Consistency is checked only against the neighbours that have already been coloured; this is the minimum constraint check required for correctness.

### 2.2 Why the Australia map is 3-colourable

The dual graph of the seven regions is planar and has maximum degree 5. By the Four-Colour Theorem it is 4-colourable; in practice the instance is also 3-colourable (the solution found by the solver is a concrete witness). Tasmania has degree 0, so it never participates in any constraint.

### 2.3 Test-case design (CSP)

| Test            | Mind-map category                         | Why it was chosen                                                                 |
|-----------------|-------------------------------------------|-----------------------------------------------------------------------------------|
| `test_given_example` | Solvable / typical                    | Full Australia map with the standard 3-colour domain.                             |
| `test_case_1`   | Edge / unconstrained variable             | Tasmania has an empty neighbour list; every colour must be accepted.              |
| `test_case_2`   | Constraint-violation detection            | Checks both rejection of a conflicting colour and acceptance of a legal colour.   |
| `test_case_3`   | Unsolvable / over-constrained             | Domain reduced to a single colour; search must return `None`.                     |

Again the three categories are orthogonal: an unconstrained variable, a partial-assignment conflict check, and a globally unsatisfiable instance.

---

## 3. Reflection

- An admissible heuristic is the key guarantee that A* returns optimal paths; Manhattan distance satisfies the definition for 4-connected grids.
- Stopping only when the goal is *popped* (not when it is first generated) is required for that optimality guarantee.
- CSP backtracking is correct as long as consistency is checked against already-assigned neighbours and failed assignments are properly undone.
- Good test design means choosing cases that exercise different regions of the “mind-map” (happy path, boundary, negative) rather than three slight variations of the same scenario. That is what the three tests for each assignment attempt to do.