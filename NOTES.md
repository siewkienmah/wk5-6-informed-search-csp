## Week 5 — Heuristic Admissibility

The Manhattan-distance heuristic is admissible because movement is limited to the four cardinal directions and each move costs one. Reaching the goal requires at least the remaining horizontal and vertical distance, while walls can only make the true path longer, so the heuristic never overestimates the optimal cost. When two nodes have the same `f` value, my implementation prefers the larger `g` value and then the lexicographically smaller `(row, column)` position.

## Week 6 — Mind-Map Coverage

The three required A* tests cover Structure → complex and Correctness → optimality with a forced detour, Boundary Conditions → start equals goal, and Solvability → unsolvable together with Correctness → failure handling for a blocked goal. The three required CSP tests cover Boundary Conditions → single variable, Correctness → validity by checking all assigned neighbours, and Solvability → unsolvable with a two-colour triangle. I chose this spread so each file tests three distinct branches—a structural or correctness case, a boundary case, and a failure case—instead of repeating similar successful inputs.

## Optional Polish and Bonuses

An additional large open-grid test covers the previously unused Input Size → large/stress branch, while another test confirms that `ASSIGNMENT_GRID` has the optimal cost of 13 and directly checks the required `heuristic` and `neighbours` helpers. The optional diagonal mode uses unit-cost diagonal moves and the Chebyshev-distance heuristic, which remains admissible and consistent for eight-directional movement. For the unsatisfiable two-colour triangle, plain backtracking explores 5 recursive states while forward checking explores 3, pruning 2 states as soon as a remaining domain becomes empty. On the Australia map itself both explore 8 states, since the default ordering never empties a domain early; the pruning advantage only appears on over-constrained problems such as the triangle (5→3) and K4 with three colours (16→10).
