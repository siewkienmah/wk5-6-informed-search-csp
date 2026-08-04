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
    r, c = node
    # 上、下、左、右 四个方向
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        # is_walkable 是模板自带函数，会自动判断是否越界以及是否是墙 '#'
        if is_walkable(grid, nr, nc):
            yield (nr, nc)


def heuristic(node, goal):
 
    r1, c1 = node
    r2, c2 = goal
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
    # 1. 初始化数据结构
    h_start = heuristic(start, goal)
    # 优先队列中的元组：(f, -g, row, col, node) -> 用 -g 打破平局，优先拓展走得更远的节点
    open_list = [(h_start, 0, start[0], start[1], start)]
    g_score = {start: 0}
    came_from = {}
    closed_set = set()

    # 2. 搜索主循环
    while open_list:
        f, neg_g, r, c, current = heapq.heappop(open_list)

        if current in closed_set:
            continue

        # POP 出 goal 时说明找到了最优路径
        if current == goal:
            return reconstruct_path(came_from, current), g_score[current]

        closed_set.add(current)

        # 遍历邻居
        for nxt in neighbours(grid, current):
            if nxt in closed_set:
                continue

            tentative_g = g_score[current] + 1

            if nxt not in g_score or tentative_g < g_score[nxt]:
                g_score[nxt] = tentative_g
                came_from[nxt] = current
                f_nxt = tentative_g + heuristic(nxt, goal)
                # 将新节点压入优先队列
                heapq.heappush(open_list, (f_nxt, -tentative_g, nxt[0], nxt[1], nxt))

    # 3. 循环结束仍未到达 goal，说明无解
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