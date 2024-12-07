count = 0
with open("input.txt", "r") as file:
    word_search = [line.strip() for line in file.readlines()]

length = len(word_search)
directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]

for i, x in enumerate(word_search):
    for j, y in enumerate(x):
        if y == "X":
            for di, dj in directions:
                if (
                    0 <= i + 3 * di < length
                    and 0 <= j + 3 * dj < length
                    and word_search[i + di][j + dj] == "M"
                    and word_search[i + 2 * di][j + 2 * dj] == "A"
                    and word_search[i + 3 * di][j + 3 * dj] == "S"
                ):
                    count += 1
print("first part:", count)

count2 = 0

d: dict[str, str] = {"M": "S", "S": "M"}

for i, x in enumerate(word_search):
    for j, y in enumerate(x):
        if y == "A":
            if 0 < i < (length - 1) and 0 < j < (length - 1):
                for k, v in d.items():
                    if (
                        word_search[i - 1][j - 1] == k
                        and word_search[i + 1][j + 1] == v
                    ):
                        if (
                            word_search[i - 1][j + 1] == k
                            and word_search[i + 1][j - 1] == v
                        ) or (
                            word_search[i - 1][j + 1] == v
                            and word_search[i + 1][j - 1] == k
                        ):
                            count2 += 1
print("second part: ", count2)


# import re
# import numpy as np
#
# with open("input2.txt", "r") as f:
#     lines = f.readlines()
# lines = [line.strip() for line in lines]
# res = 0
# for line in lines:
#     res += len(re.findall("XMAS|SAMX", line))
#
# lines_split = np.array([list(line) for line in lines])
#
# cols = ["".join(col) for col in np.transpose(lines_split)]
#
# for col in cols:
#     res += len(re.findall("XMAS|SAMX", col))
#
# for i in range(len(lines)):
#     for j in range(len(lines[i])):
#         if (
#             lines[i][j] == "X"
#             and i <= (len(lines) - 4)
#             and j <= (len(lines[i]) - 4)
#             and lines[i + 1][j + 1] == "M"
#             and lines[i + 2][j + 2] == "A"
#             and lines[i + 3][j + 3] == "S"
#         ):
#             res += 1
#         if (
#             lines[i][j] == "X"
#             and j >= 3
#             and i <= (len(lines[i]) - 4)
#             and lines[i + 1][j - 1] == "M"
#             and lines[i + 2][j - 2] == "A"
#             and lines[i + 3][j - 3] == "S"
#         ):
#             res += 1
#         if (
#             lines[i][j] == "S"
#             and i <= (len(lines) - 4)
#             and j <= (len(lines[i]) - 4)
#             and lines[i + 1][j + 1] == "A"
#             and lines[i + 2][j + 2] == "M"
#             and lines[i + 3][j + 3] == "X"
#         ):
#             res += 1
#         if (
#             lines[i][j] == "S"
#             and j >= 3
#             and i <= (len(lines[i]) - 4)
#             and lines[i + 1][j - 1] == "A"
#             and lines[i + 2][j - 2] == "M"
#             and lines[i + 3][j - 3] == "X"
#         ):
#             res += 1
#
#
# print(res)
