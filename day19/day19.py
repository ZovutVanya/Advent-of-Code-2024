from functools import cache


@cache
def possible(design, towels):
    if not design:
        return 1
    return sum(
        possible(design[len(towel):], towels)
        for towel in towels
        if design.startswith(towel)
    )


data = open("input.txt")
towels = tuple(data.readline().rstrip().split(", "))
designs = data.read().split()
pos = [possible(design, towels) for design in designs]
print(sum(map(bool, pos)))
print(sum(pos))
