# Notes

Manhattan distance is admissible for this 4-directional grid because it counts the minimum number of horizontal and vertical moves needed to reach the goal when each move costs 1. Walls can only make the actual route longer, never shorter, so the Manhattan distance never overestimates the true remaining cost.

For A*, the three test cases cover a typical solvable grid, the boundary case where the start equals the goal and an unsolvable grid. For CSP, the three test cases cover a small solvable constraint structure, the single-variable boundary case and an unsolvable triangle with too few colours. This gives coverage across different mind-map branches instead of repeating similar happy-path tests.
