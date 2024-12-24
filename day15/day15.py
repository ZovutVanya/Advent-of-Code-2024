from collections import defaultdict
from collections.abc import Iterable
from typing import TypeAlias


Grid: TypeAlias = defaultdict[complex, str]
OFFSETS: dict[str, complex] = {
    ">": 1 + 0j,
    "<": -1 + 0j,
    "v": 1j,
    "^": -1j,
}
WIDE_TILES = {".": "..", "#": "##", "O": "[]"}


def part1(lines: Iterable[str]) -> int:
    line_iter = iter(lines)
    grid: Grid = defaultdict(lambda: "#")
    robot: complex | None = None
    for y, row in enumerate(line_iter):
        if not row:
            break
        for x, tile in enumerate(row):
            pos = x + y * 1j
            if tile == "@":
                robot, tile = pos, "."
            grid[pos] = tile
    assert robot is not None
    movements = "".join(line_iter)

    for movement in movements:
        offset = OFFSETS.get(movement, 0j)
        new_robot = robot + offset

        new_robot_tile = grid[new_robot]
        if new_robot_tile == "#":
            continue
        elif new_robot_tile == "O":
            box = new_robot
            while (tile := grid[box]) == "O":
                box += offset
            if tile == "#":
                continue

            grid[box], grid[new_robot] = grid[new_robot], tile

        robot = new_robot

    return sum(
        100 * int(pos.imag) + int(pos.real) for pos, tile in grid.items() if tile == "O"
    )


def part2(lines: Iterable[str]) -> int:
    from collections import deque

    WIDE_BOX = WIDE_TILES["O"]

    line_iter = iter(lines)
    grid: defaultdict[complex, str] = defaultdict(lambda: "#")
    robot: complex | None = None
    for y, row in enumerate(line_iter):
        if not row:
            break
        for x, tile in enumerate(row):
            pos = x * 2 + y * 1j
            if tile == "@":
                robot, tile = pos, "."
            for w, wide_tile in enumerate(WIDE_TILES.get(tile, WIDE_TILES["."])):
                grid[pos + w] = wide_tile
    assert robot is not None
    movements = "".join(line_iter)

    for movement in movements:
        offset = OFFSETS.get(movement, 0j)
        new_robot = robot + offset

        new_robot_tile = grid[new_robot]
        robot_is_pushing = new_robot_tile in WIDE_BOX
        if new_robot_tile == "#":
            continue
        elif robot_is_pushing and movement in "<>":
            box = new_robot
            while (tile := grid[box]) in WIDE_BOX:
                box += offset
            if tile == "#":
                continue

            while box != new_robot:
                grid[box] = grid[box - offset]
                box -= offset
            grid[new_robot] = tile
        elif robot_is_pushing and movement in "^v":
            boxes_to_push: dict[complex, None] = {}
            box = new_robot
            while grid[box] != WIDE_BOX[0]:
                box -= 1
            box_queue = deque([box])
            while box_queue:
                box = box_queue.popleft()
                boxes_to_push[box] = None
                for w in range(len(WIDE_BOX)):
                    in_front_of_box = box + w + offset
                    if grid[in_front_of_box] == "#":
                        box_queue.clear()
                        boxes_to_push.clear()
                        break
                    elif grid[in_front_of_box] in WIDE_BOX:
                        while grid[in_front_of_box] != WIDE_BOX[0]:
                            in_front_of_box -= 1
                        boxes_to_push[in_front_of_box] = None
                        box_queue.append(in_front_of_box)
            if not boxes_to_push:
                continue

            for box in reversed(boxes_to_push):
                for w in range(len(WIDE_BOX)):
                    grid[box + w + offset], grid[box + w] = (
                        grid[box + w],
                        grid[box + w + offset],
                    )

        robot = new_robot

    return sum(
        100 * int(pos.imag) + int(pos.real)
        for pos, char in grid.items()
        if char == WIDE_BOX[0]
    )


with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

print("Part 1", part1(lines), "\nPart 2", part2(lines))
