with open("input.txt", "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]
# for line in lines:
#     print("".join(line))

antennas = set([row for col in lines for row in col])
antennas.remove('.')

antennas_coords: dict[str, list] = {antenna: [] for antenna in antennas}

for i, line in enumerate(lines):
    for j, point in enumerate(line):
        if point in antennas:
            antennas_coords[point].append(tuple([i, j]))

for antenna, coords in antennas_coords.items():
    for idx, (i1, j1) in enumerate(coords):
        for i2, j2 in coords[idx+1:]:
            for multiplier in range(50):
                flag1 = False
                flag2 = False
                if j1 < j2:
                    antinode_coord = tuple([2*i1-i2, j1*2-j2])
                    another_one = tuple([2*i2-i1, j2*2-j1])
                else:
                    antinode_coord = tuple([2*i1-i2, j1*2-j2])
                    another_one = tuple([2*i2-i1, j2*2-j1])
                antinode_i = antinode_coord[0]-(i2-i1)*multiplier
                antinode_j = antinode_coord[1]+(j1-j2)*multiplier
                another_i = another_one[0]+(i2-i1)*multiplier
                another_j = another_one[1]+(j2-j1)*multiplier
                if antinode_i >= 0 and antinode_j >= 0:
                    try:
                        lines[antinode_i][antinode_j] = "#"
                    except Exception:
                        flag1 = True
                if another_i >= 0 and another_j >= 0:
                    try:
                        lines[another_i][another_j] = "#"
                    except Exception:
                        flag2 = True
                if flag1 is True and flag2 is True:
                    break


flat = [row for col in lines for row in col]
res = flat.count("#")
for antenna in antennas:
    if len(antennas_coords[antenna]) > 1:
        res += flat.count(antenna)
print(res)

# for line in lines:
#     print("".join(line))
