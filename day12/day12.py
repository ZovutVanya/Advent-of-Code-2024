from collections import deque

with open("input.txt", "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]

for line in lines:
    print("".join(line))

directions = {(0, -1), (0, 1), (-1, 0), (1, 0)}

# lines_flat = [row for col in lines for row in col]
# letterset = set(lines_flat)


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
            if (
                isMappable(new_row, new_col, lines)
                and lines[new_row][new_col] == char
            ):
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


def dfs():
    pass
