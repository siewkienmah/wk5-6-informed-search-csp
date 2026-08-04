import heapq

def heuristic(a: tuple[int, int], b: tuple[int, int]) -> int:
    """
    Calculates Manhattan distance between two grid points.
    Formula: |x1 - x2| + |y1 - y2|
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def neighbours(grid: list[str], node: tuple[int, int]) -> list[tuple[int, int]]:
    """
    Returns valid 4-directional neighbours (Up, Down, Left, Right)
    that are within grid boundaries and not wall cells ('#').
    """
    r, c = node
    rows = len(grid)
    cols = len(grid[0])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    valid_neighbours = []
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] != '#':
                valid_neighbours.append((nr, nc))
                
    return valid_neighbours


def astar(grid: list[str], start: tuple[int, int], goal: tuple[int, int]):
    """
    Performs A* Search to find the shortest path from start to goal in a grid.
    Returns: (path, cost) or (None, infinity) if no path exists.
    """
    if start == goal:
        return [start], 0

    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), start))
    
    came_from = {}
    g_score = {start: 0}
    closed_set = set()

    while open_set:
        current_f, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            curr = goal
            while curr in came_from:
                path.append(curr)
                curr = came_from[curr]
            path.append(start)
            path.reverse()
            return path, g_score[goal]

        if current in closed_set:
            continue
        closed_set.add(current)

        for nxt in neighbours(grid, current):
            if nxt in closed_set:
                continue

            tentative_g = g_score[current] + 1

            if nxt not in g_score or tentative_g < g_score[nxt]:
                came_from[nxt] = current
                g_score[nxt] = tentative_g
                f_score = tentative_g + heuristic(nxt, goal)
                heapq.heappush(open_set, (f_score, nxt))

    return None, float('inf')