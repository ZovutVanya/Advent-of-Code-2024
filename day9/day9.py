with open("input.txt", "r") as f:
    line = f.readline().strip()


def line2blocks(line: str):
    blocks = []
    for i, char in enumerate(line):
        if i % 2 == 0:
            blocks.append(int(char) * [i - i // 2])
        else:
            blocks.append(int(char) * ["."])
    return blocks


blocks = line2blocks(line)

print(blocks, "\n")

blanks = blocks[1::2]
files = blocks[0::2]
files_flat = [row for col in files for row in col]
blocks_flat = [row for col in blocks for row in col]

# for i, point in enumerate(blocks_flat):
#     if point == ".":
#         blocks_flat[i] = files_flat[-1]
#         files_flat.pop(-1)
#         blocks_flat.pop(-1)
#
# while len([row for col in blocks[0::2] for row in col]) != len(blocks_flat):
#     blocks_flat.pop(-1)
#
# res = 0
# for i, num in enumerate(blocks_flat):
#     res += i*num
#
# print(res)

print(files, "\n")
print(blanks, "\n")

len_files = len(files)

for j, file in enumerate(files[::-1]):
    for i, blank in enumerate(blanks):
        if len(file) <= blank.count(".") and len_files-j > i+1:
            for f in file:
                blank[blank.index(".")] = f
            blocks[(1 * i) + 1] = blank
            files[-1 * (j + 1)] = ["."] * len(files[-1 * (j + 1)])
            break
print(files, "\n")
print(blanks, "\n")

final = []
for file in files:
    final.append(file)
    for i, blank in enumerate(blanks):
        # if set(blank) != {"."}:
        final.append(blank)
        blanks.pop(i)
        break

final_flat = [row for col in final for row in col]
print(final_flat)

res = 0
for i, whatever in enumerate(final_flat):
    if whatever != ".":
        res += i * whatever

print(res)
