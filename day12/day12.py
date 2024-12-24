from collections import deque

with open("input.txt", "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]

directions = {(0, -1), (0, 1), (-1, 0), (1, 0)}


def isMappable(i, j, grid) -> bool:
    return 0 <= i < len(grid) and 0 <= j < len(grid[i])


rows = len(lines)
cols = len(lines[0])
visited = [[False for _ in range(cols)] for _ in range(rows)]


def bfs(row: int, col: int, char: str):
    queue = deque([(row, col)])
    visited[row][col] = True
    area = 0
    perimeter = 0

    while queue:
        current_row, current_col = queue.popleft()
        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc
            if isMappable(new_row, new_col, lines) and lines[new_row][new_col] == char:
                perimeter -= 1
                if not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col))
        area += 1
        perimeter += 4
    return area, perimeter


total_cost = 0
for row in range(rows):
    for col in range(cols):
        if not visited[row][col]:
            # print(lines[row][col])
            area, perimeter = bfs(row, col, lines[row][col])
            # print(area, perimeter)
            total_cost += area * perimeter

print(total_cost)

data = open("input.txt").read().splitlines()

G = {(i) + (j) * 1j: e for i, row in enumerate(data) for j, e in enumerate(row)}


def dfs(p, e, region, fence, dr=None):
    if p in viz and G.get(p) == e:
        return
    if G.get(p) != e:
        return fence.add((p, dr))
    viz.add(p), region.add(p)
    for dr in dirs:
        dfs(p + dr, e, region, fence, dr)
    neighbors = {(p + dr * 1j, dr) for p, dr in fence}
    return len(region), len(fence), len(fence - neighbors)


dirs, viz = (1, -1, 1j, -1j), set()

regions = [dfs(p, e, set(), set()) for p, e in G.items() if p not in viz]

print(sum(area * perim for area, perim, _ in regions))
print(sum(area * sides for area, _, sides in regions))
