# Notes — A* Search and CSP

## A* Heuristic Admissibility

The heuristic used in the A* search is Manhattan distance, calculated as the sum of the absolute row and column differences between the current node and the goal. Because movement is limited to four directions, Manhattan distance never overestimates the actual minimum number of moves needed to reach the goal. Therefore, the heuristic is admissible.

## Test Case Coverage

My six test cases cover the mind-map branches of solvability, including solvable and unsolvable/over-constrained cases, as well as edge/boundary cases. I chose this spread to test normal behaviour, failure conditions, and minimum-input situations rather than repeatedly testing the same type of successful case.