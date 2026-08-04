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
    """TODO: yield the valid 4-directional neighbours of `node` in `grid`.

    `node` is a (row, col) tuple. A neighbour is valid if is_walkable()
    returns True for it. Use up/down/left/right moves only (no diagonals).
    """
    row, col = node
    for r, c in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
        if is_walkable(grid, r, c):
            yield (r, c)


def heuristic(node, goal):
    """TODO: return the Manhattan distance between `node` and `goal`.

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
    """TODO: implement the A* algorithm.

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
    open_heap = [(heuristic(start, goal), 0, start)]
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

        for neighbour in neighbours(grid, node):
            if neighbour in closed:
                continue
            tentative_g = g_score[node] + 1
            if tentative_g < g_score.get(neighbour, float('inf')):
                g_score[neighbour] = tentative_g
                came_from[neighbour] = node
                f_score = tentative_g + heuristic(neighbour, goal)
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
