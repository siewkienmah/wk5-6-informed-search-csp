# NOTES — Weeks 5 & 6 (A* Search and CSP)

## Heuristic admissibility

My A* solver uses Manhattan distance, `h(n) = |r1 - r2| + |c1 - c2|`. Movement is
restricted to 4 directions with every step costing exactly 1, so any route from a
cell to the goal must change the row `|Δrow|` times and the column `|Δcol|` times —
meaning it cannot possibly take fewer than `|Δrow| + |Δcol|` moves. Walls and
detours can only force *extra* moves, never fewer, so `h` never overestimates the
true remaining cost and is therefore admissible, which is what guarantees A*
returns an optimal path.

Manhattan distance here is additionally **consistent** (monotone): moving to an
adjacent cell costs 1 and changes `h` by at most 1, so `h(n) ≤ c(n, n') + h(n')`
always holds. This matters because my implementation keeps a closed set and never
re-expands a node once it has been popped — that shortcut is only safe under
consistency, not under admissibility alone. (If I later reuse this solver on the
weighted road graph in my main assignment, straight-line distance stays admissible
only while no edge weight is *less* than the straight-line distance between its
endpoints, so that assumption has to be re-checked there.)

## Test case coverage

| Test | File | Mind-map branch(es) covered |
|---|---|---|
| `test_case_1` | A* | Structure → complex (walls); Solvability → solvable; Correctness → optimality |
| `test_case_2` | A* | Boundary Conditions → start equals goal (zero-move minimal case) |
| `test_case_3` | A* | Solvability → unsolvable (goal walled off); Correctness → failure handling |
| `test_case_1` | CSP | Solvability → unsolvable / over-constrained (K4 on 3 colours); Correctness → failure handling |
| `test_case_2` | CSP | Boundary Conditions → single variable; Input Size → trivial smallest input |
| `test_case_3` | CSP | Structure → symmetric (9-region odd ring); Input Size → larger; Correctness → validity |

Across the two algorithms my six tests draw on five of the mind-map's branches —
Structure, Solvability, Boundary Conditions, Input Size, and all three "What
You're Actually Checking" leaves (optimality, validity, failure handling) — rather
than repeating one branch six times. I picked this spread because the three things
that most commonly break a search or CSP implementation are each covered
independently: the happy path proves it finds a *correct and optimal* answer, the
boundary cases prove it doesn't miscount or loop when the input is degenerate
(start = goal, a single variable), and the unsolvable cases prove it terminates and
reports failure cleanly instead of crashing or returning a partial result. The two
unsolvable tests are deliberately different in kind — the A* one is unreachable
because of physical walls, the CSP one because the problem is over-constrained —
so they exercise failure handling for two genuinely different reasons.

I also chose the CSP over-constrained case as K4-on-3-colours rather than the
triangle-on-2-colours already hand-traced in `02_CSP/worked_example.md`, so that
the test checks a configuration that wasn't handed to me, and I paired it with the
same graph on 4 colours to confirm the `None` result is real over-constraint rather
than a broken solver.

## Verification beyond the required tests

As a correctness check I cross-checked both solvers against independent oracles:
A* against a breadth-first search (which gives the true optimal cost on a unit-cost
grid) over 400 randomly generated grids, and the CSP solver against exhaustive
enumeration of every possible assignment over 300 randomly generated graphs. Zero
mismatches in both cases.

## Bonus items not attempted

Diagonal movement for A* and forward checking for the CSP are marked optional in
`assignments/assignment_wk5_6.md` and are not implemented here.
