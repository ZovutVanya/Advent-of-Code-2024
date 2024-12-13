with open("input.txt", "r") as f:
    lines = [[int(num) for num in list(line.strip())] for line in f.readlines()]

for line in lines:
    print(line)

directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

trailheads = []
for i, line in enumerate(lines):
    for j, n in enumerate(line):
        if n == 0:
            trailheads.append((i, j))

print(trailheads)

paths = []

gh = len(lines)
gw = len(lines[0])


def dfs(grid, x, y, path, visited, target, reached_nines):
    if grid[x][y] == 9 and target == 9:
        reached_nines.add((x, y))
        paths.append(path)
        return

    visited.add((x, y))

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < gh and 0 <= ny < gw and (nx, ny) not in visited:
            if grid[nx][ny] == target + 1:
                dfs(grid, nx, ny, path + [(nx, ny)], visited, target + 1, reached_nines)

    visited.remove((x, y))


results = {}

for trailhead in trailheads:
    unique_nines: set[tuple[int, int]] = set()
    dfs(lines, trailhead[0], trailhead[1], [trailhead], set(), 0, unique_nines)
    results[trailhead] = unique_nines

print(sum([len(nines) for nines in results.values()]))
print(len(paths))
