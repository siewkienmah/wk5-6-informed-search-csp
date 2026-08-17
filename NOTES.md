# Submission Notes

## Heuristic Admissibility
The Manhattan distance heuristic $h(n) = |x_1 - x_2| + |y_1 - y_2|$ is admissible for 4-directional grid movement because it calculates the shortest straight orthogonal distance without considering obstacles. Because each move in the grid costs 1 unit, Manhattan distance never overestimates the actual remaining cost to the goal ($h(n) \le h^*(n)$), ensuring A* always finds an optimal path.

## Test Case Coverage
The 6 test cases across both modules cover distinct structural and solvability branches from the mind-map:
1. **A* Search**: Covered detours around wall obstacles, completely enclosed/unreachable goals (returning `inf`), and identical start/goal edge cases.
2. **CSP Map Colouring**: Covered unsolvable over-constrained domains (2-colour failure), trivial single-node graphs ("T"), and smaller fully-connected sub-maps (WA-NT-SA).