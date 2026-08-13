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


def neighbours(grid, node, allow_diagonal=False):
    """Yield the valid neighbours of `node` in `grid`.

    `node` is a (row, col) tuple. A neighbour is valid if is_walkable()
    returns True for it. Movement is up/down/left/right by default; set
    `allow_diagonal` to True to include the four diagonal moves.
    """
    row, col = node
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if allow_diagonal:
        directions.extend([(-1, -1), (-1, 1), (1, -1), (1, 1)])

    for row_change, col_change in directions:
        r, c = row + row_change, col + col_change
        if is_walkable(grid, r, c):
            yield (r, c)


def heuristic(node, goal, allow_diagonal=False):
    """Return an admissible distance estimate from `node` to `goal`.

    node and goal are (row, col) tuples.
    Manhattan distance is used for four-directional movement. Chebyshev
    distance is used when unit-cost diagonal movement is enabled.
    """
    row_distance = abs(node[0] - goal[0])
    col_distance = abs(node[1] - goal[1])
    if allow_diagonal:
        return max(row_distance, col_distance)
    return row_distance + col_distance


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


def astar(grid, start, goal, allow_diagonal=False):
    """Run the A* algorithm from `start` to `goal` on `grid`.

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
    open_heap = [(heuristic(start, goal, allow_diagonal), 0, start)]
    g_score = {start: 0}
    came_from = {}
    closed = set()

    while open_heap:
        f, neg_g, node = heapq.heappop(open_heap)

        if node == goal:
            path = reconstruct_path(came_from, node)
            return path, g_score[node]

        if node in closed:
            continue
        closed.add(node)

        for neighbour in neighbours(grid, node, allow_diagonal):
            if neighbour in closed:
                continue
            tentative_g = g_score[node] + 1
            if tentative_g < g_score.get(neighbour, float('inf')):
                g_score[neighbour] = tentative_g
                came_from[neighbour] = node
                f_score = tentative_g + heuristic(
                    neighbour, goal, allow_diagonal
                )
                heapq.heappush(open_heap, (f_score, -tentative_g, neighbour))

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
