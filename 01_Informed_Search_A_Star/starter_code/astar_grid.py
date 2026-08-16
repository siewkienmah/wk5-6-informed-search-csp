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
    """Yield valid 4-directional neighbours of node."""

    r, c = node

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if is_walkable(grid, nr, nc):
            yield (nr, nc)


def heuristic(node, goal):
    """Return the Manhattan distance between `node` and `goal`."""
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
    """Implement the A* algorithm."""

    open_list = []

    # f = g + h
    heapq.heappush(
        open_list,
        (heuristic(start, goal), 0, start)
    )

    g_score = {start: 0}
    came_from = {}
    closed = set()

    while open_list:
        f, neg_g, current = heapq.heappop(open_list)

        # Convert negative g back to normal g
        g = -neg_g

        if current in closed:
            continue

        # Stop when the goal is removed from OPEN
        if current == goal:
            path = reconstruct_path(came_from, current)
            return path, g

        closed.add(current)

        for neighbour in neighbours(grid, current):

            if neighbour in closed:
                continue

            new_g = g + 1

            if new_g < g_score.get(neighbour, float("inf")):

                g_score[neighbour] = new_g
                came_from[neighbour] = current

                h = heuristic(neighbour, goal)
                f = new_g + h

                heapq.heappush(
                    open_list,
                    (f, -new_g, neighbour)
                )

    return None, float("inf")