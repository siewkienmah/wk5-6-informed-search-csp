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
    """TODO: yield the valid 4-directional neighbours of `node` in `grid`."""
    r, c = node
    possible = [
        (r-1, c),  # up
        (r+1, c),  # down
        (r, c-1),  # left
        (r, c+1)   # right
    ]
    result = []
    for nr, nc in possible:
        if is_walkable(grid, nr, nc):
            result.append((nr, nc))
    return result


def heuristic(node, goal):
    """TODO: return the Manhattan distance between `node` and `goal`."""
    r1, c1 = node
    r2, c2 = goal
    return abs(r1 - r2) + abs(c1 - c2)


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
    """TODO: implement the A* algorithm."""
    import heapq
    
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    closed_set = set()
    
    while open_set:
        f_score, current = heapq.heappop(open_set)
        
        if current in closed_set:
            continue
        
        if current == goal:
            path = reconstruct_path(came_from, current)
            return (path, g_score[goal])
        
        closed_set.add(current)
        
        for neighbor in neighbours(grid, current):
            if neighbor in closed_set:
                continue
            
            new_g = g_score[current] + 1
            
            if neighbor not in g_score or new_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = new_g
                f_score = new_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))
    
    return (None, float('inf'))


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
