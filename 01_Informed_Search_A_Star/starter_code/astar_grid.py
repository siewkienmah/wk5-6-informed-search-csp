"""
Assignment starter: A* search on a grid.

Read ../guide.md and ../worked_example.md BEFORE you start coding here.

Your job: fill in every function marked TODO. Do not change function
signatures (the tests in test_astar_grid.py rely on them).

Grid legend:
    'S' = start
    'G' = goal
    '#' = wall (cannot be entered)
    '.' = free cell

Run this file directly to see your solver in action:
    python astar_grid.py
"""
import heapq

# The assignment grid. Do not edit this -- your solver must work on this
# AND on any other valid grid (the test file uses different grids too).
ASSIGNMENT_GRID = [
    "S.......",
    ".#..#.#.",
    ".#....#.",
    ".###.##.",
    "...#....",
    "##.#.##.",
    ".....#..",
    ".##...G.",
]

ROWS = len(ASSIGNMENT_GRID)
COLS = len(ASSIGNMENT_GRID[0])


def find_cell(grid, symbol):
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == symbol:
                return (r, c)
    raise ValueError(f"Symbol {symbol!r} not found in grid")


def is_walkable(grid, r, c):
    """
    Return True if (r, c) is inside the grid and not a wall.
    """
    rows, cols = len(grid), len(grid[0])
    if not (0 <= r < rows and 0 <= c < cols):
        return False
    return grid[r][c] != "#"


def neighbours(grid, node):
    """
    Yield the valid 4-directional neighbours of `node` in `grid`.
    """
    r, c = node
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if is_walkable(grid, nr, nc):
            yield (nr, nc)


def heuristic(node, goal):
    """
    Return the Manhattan distance between `node` and `goal`.
    """
    r1, c1 = node
    r2, c2 = goal
    return abs(r1 - r2) + abs(c1 - c2)


def reconstruct_path(came_from, current):
    """
    Rebuild the path from start to `current` using the came_from map.
    """
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def astar(grid, start, goal):
    """Implement the A* algorithm.

    Return a tuple: (path, cost)
      - path: list of (row, col) tuples from start to goal, inclusive.
              Return None if no path exists.
      - cost: total path cost (int). Return float('inf') if no path exists.

    Follow the pseudocode in ../guide.md section 4:
      1. Use a heapq-based priority queue keyed on f(n) = g(n) + h(n).
      2. Track g_score for every discovered node.
      3. Track came_from so you can reconstruct the path.
      4. Track a closed set of fully-expanded nodes.
      5. Stop as soon as you POP the goal node from the open list
         (not merely when you first see it as a neighbour).

    Tie-break tip: pushing tuples like (f, -g, row, col, node) onto the
    heap gives you a deterministic tie-break (prefer larger g) -- see the
    worked example solution for this pattern if you get stuck.
    """
    # Priority queue entries: (f, -g, row, col, node)
    # -g prefers larger g on ties (more progress toward goal)
    open_heap = []
    g_score = {start: 0}
    came_from = {}
    closed = set()

    h0 = heuristic(start, goal)
    heapq.heappush(open_heap, (h0, 0, start[0], start[1], start))

    while open_heap:
        f, neg_g, r, c, current = heapq.heappop(open_heap)

        if current in closed:
            continue
        if current == goal:
            path = reconstruct_path(came_from, current)
            return path, g_score[current]

        closed.add(current)

        for neighbour in neighbours(grid, current):
            if neighbour in closed:
                continue
            tentative_g = g_score[current] + 1  # uniform cost of 1 per step
            if neighbour not in g_score or tentative_g < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g
                f_score = tentative_g + heuristic(neighbour, goal)
                heapq.heappush(
                    open_heap,
                    (f_score, -tentative_g, neighbour[0], neighbour[1], neighbour),
                )

    return None, float("inf")


if __name__ == "__main__":
    start = find_cell(ASSIGNMENT_GRID, "S")
    goal = find_cell(ASSIGNMENT_GRID, "G")
    print(f"Start: {start}, Goal: {goal}")

    path, cost = astar(ASSIGNMENT_GRID, start, goal)

    if path:
        print(f"Path found (cost={cost}):")
        print(" -> ".join(str(p) for p in path))
    else:
        print("No path exists.")