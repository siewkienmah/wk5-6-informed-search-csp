# Notes — Weeks 5 & 6: A* Search and CSP

## Heuristic admissibility (A*)

The A* solver uses Manhattan distance, `h(n) = |r_n - r_goal| + |c_n - c_goal|`,
as its heuristic. Because movement is restricted to 4-directional
(up/down/left/right) steps that each cost exactly 1, the minimum possible
number of moves to the goal — ignoring walls entirely — is exactly the
Manhattan distance; walls can only ever force a *longer* route, never a
shorter one. So `h(n)` can never exceed the true remaining cost
(`h(n) ≤ true cost(n → goal)` for every `n`), which is the definition of
admissible, and admissibility is what guarantees A* returns the optimal
path.

## Test case coverage (6 test cases total)

Across the two exercises, the 6 test cases span 5 different mind-map
branches rather than repeating one: **Boundary Conditions** (A*'s
start=goal case; CSP's unconstrained Tasmania variable with no
neighbours), **Structure** (A*'s obstacles forcing a detour; CSP's dense
WA-NT-SA triangle), **Solvability → unsolvable** (A*'s sealed-off goal;
CSP's map with only 2 colours available), **Correctness → Optimality**
(A*'s obstacle-path cost is hand-verified against the Manhattan lower
bound of 6), and **Correctness → Validity** (CSP's direct
conflict-detection check on `is_consistent`). This spread was chosen so
the tests catch genuinely different failure modes — an off-by-one at a
boundary, a wrong route around obstacles, a broken no-path/no-solution
termination, and a broken constraint check — instead of 6 variations of
the same happy-path scenario.
