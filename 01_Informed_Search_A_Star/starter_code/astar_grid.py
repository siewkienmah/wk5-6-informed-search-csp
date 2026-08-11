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
    """Return the (row, col) of `symbol` in `grid`. Already implemented."""
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == symbol:
                return (r, c)
    raise ValueError(f"Symbol {symbol!r} not found in grid")


def is_walkable(grid, r, c):
    """Return True if (r, c) is inside the grid and not a wall.

    Already implemented -- use this inside your neighbours() function.
    """
    rows, cols = len(grid), len(grid[0])
    if not (0 <= r < rows and 0 <= c < cols):
        return False
    return grid[r][c] != "#"


def neighbours(grid, node):
    """Yield the valid 4-directional neighbours of `node` in `grid`.

    `node` is a (row, col) tuple. A neighbour is valid if is_walkable()
    returns True for it. Use up/down/left/right moves only (no diagonals).
    """
    r, c = node
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if is_walkable(grid, nr, nc):
            yield (nr, nc)


def heuristic(node, goal):
    """Return the Manhattan distance between `node` and `goal`.

    node and goal are (row, col) tuples.
    Manhattan distance = |row1 - row2| + |col1 - col2|.
    This must be admissible for 4-directional grid movement -- explain in
    your submission notes why Manhattan distance satisfies this.
    """
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


def reconstruct_path(came_from, current):
    """Rebuild the path from start to `current` using the came_from map.

    Already implemented.
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
    """
    g_score = {start: 0}
    came_from = {}
    closed_set = set()

    # Heap tuple structure for deterministic tie-breaking: (f_score, -g_score, row, col, node)
    initial_f = heuristic(start, goal)
    open_heap = [(initial_f, 0, start[0], start[1], start)]

    while open_heap:
        f, neg_g, r, c, current = heapq.heappop(open_heap)

        if current in closed_set:
            continue

        # Stop as soon as goal is popped from the open list
        if current == goal:
            path = reconstruct_path(came_from, current)
            return path, g_score[current]

        closed_set.add(current)

        for nbr in neighbours(grid, current):
            if nbr in closed_set:
                continue

            tentative_g = g_score[current] + 1

            if nbr not in g_score or tentative_g < g_score[nbr]:
                g_score[nbr] = tentative_g
                came_from[nbr] = current
                h = heuristic(nbr, goal)
                f_score = tentative_g + h
                heapq.heappush(open_heap, (f_score, -tentative_g, nbr[0], nbr[1], nbr))

    return None, float('inf')


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