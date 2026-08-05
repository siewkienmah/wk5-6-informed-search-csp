"""
Assignment starter: A* search on a grid.

Read ../guide.md and ../worked_example.md BEFORE you start coding here.

Your job: fill in every function marked TODO. Do not change function
signatures (the tests in test_astar_grid.py rely on them).
"""
import heapq


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
    """Return the (row, col) of `symbol` in `grid`."""
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == symbol:
                return (r, c)

    raise ValueError(f"Symbol {symbol!r} not found in grid")


def is_walkable(grid, r, c):
    """Return True if (r, c) is inside the grid and not a wall."""
    rows, cols = len(grid), len(grid[0])

    if not (0 <= r < rows and 0 <= c < cols):
        return False

    return grid[r][c] != "#"


def neighbours(grid, node):
    """Yield valid up, down, left and right neighbours."""
    row, col = node

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1),   # right
    ]

    for row_change, col_change in directions:
        new_row = row + row_change
        new_col = col + col_change

        if is_walkable(grid, new_row, new_col):
            yield (new_row, new_col)


def heuristic(node, goal):
    """Return the Manhattan distance from node to goal."""
    row1, col1 = node
    row2, col2 = goal

    return abs(row1 - row2) + abs(col1 - col2)


def reconstruct_path(came_from, current):
    """Rebuild the path from start to current."""
    path = [current]

    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.reverse()
    return path


def astar(grid, start, goal):
    """Find the shortest path from start to goal using A* search."""

    open_list = []

    start_g = 0
    start_f = start_g + heuristic(start, goal)

    heapq.heappush(
        open_list,
        (start_f, -start_g, start[0], start[1], start)
    )

    came_from = {}
    g_score = {start: 0}
    closed = set()

    while open_list:
        current_f, negative_g, row, col, current = heapq.heappop(open_list)

        if current in closed:
            continue

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

                f_score = tentative_g + heuristic(neighbour, goal)

                heapq.heappush(
                    open_list,
                    (
                        f_score,
                        -tentative_g,
                        neighbour[0],
                        neighbour[1],
                        neighbour,
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
