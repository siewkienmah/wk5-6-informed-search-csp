# NOTES
## A* Heuristic
I used Manhattan distance as the heuristic for A*. It never gives a distance that is longer than the real shortest path. Since the grid only allows moving up, down, left and right, Manhattan distance is a good and valid choice.

## Test Case Coverage
For A*, I tested a normal case, an edge case, and an unsolvable case. This helps check that the algorithm works in different situations, not only one type of problem.

For CSP, I tested a constraint checking case, a boundary case using Tasmania, and an unsolvable case with only two colours. These test cases cover different situations and help make sure the program works correctly.