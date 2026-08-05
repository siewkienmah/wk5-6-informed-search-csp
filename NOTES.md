# Notes for Week 5-6 Submission

## A* Heuristic Admissibility
My heuristic uses Manhattan distance, which is admissible for 4-directional grid movement because it never overestimates the true cost. The true cost between two cells is at least the Manhattan distance since diagonal moves are not allowed, making h(n) always less than or equal to the actual cost.

## Test Case Coverage
My 6 test cases cover three different mind-map branches:
1. **Typical/Solvable cases** (test_case_1 in both exercises): Tests normal operation with obstacles (A*) and the Australia map with 3 colors (CSP).
2. **Edge cases** (test_case_3 in both exercises): Tests zero-length path (A*) and constraint verification (CSP).
3. **Unsolvable cases** (test_case_2 in both exercises): Tests no path (A*) and over-constrained with 2 colors (CSP).