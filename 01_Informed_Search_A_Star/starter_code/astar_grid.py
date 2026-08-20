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
    """Yield the valid 4-directional neighbours of node."""

    r, c = node

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc

        if is_walkable(grid, nr, nc):
            yield (nr, nc)


def heuristic(node, goal):
    """Return the Manhattan distance between node and goal."""

    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


def reconstruct_path(came_from, current):
    """Rebuild the path from start to current."""

    path = [current]

    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.reverse()
    return path


def astar(grid, start, goal):
    """Implement the A* search algorithm."""

    g_score = {start: 0}
    came_from = {}
    closed = set()

    # Heap entries: (f, -g, row, col, node)
    open_heap = []

    start_f = heuristic(start, goal)
    heapq.heappush(
        open_heap,
        (start_f, 0, start[0], start[1], start)
    )

    while open_heap:
        f, neg_g, row, col, current = heapq.heappop(open_heap)

        if current in closed:
            continue

        # Goal is reached when it is POPPED from the heap
        if current == goal:
            path = reconstruct_path(came_from, current)
            return path, g_score[current]

        closed.add(current)

        for neighbour in neighbours(grid, current):

            if neighbour in closed:
                continue

            tentative_g = g_score[current] + 1

            if tentative_g < g_score.get(neighbour, float("inf")):

                came_from[neighbour] = current
                g_score[neighbour] = tentative_g

                h = heuristic(neighbour, goal)
                f = tentative_g + h

                heapq.heappush(
                    open_heap,
                    (
                        f,
                        -tentative_g,
                        neighbour[0],
                        neighbour[1],
                        neighbour
                    )
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
