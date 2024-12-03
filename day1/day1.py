import numpy as np

with open("input.txt", "r") as f:
    lines = f.readlines()

tuples = [tuple(int(num) for num in line.strip().split()) for line in lines]

first = np.array(sorted([t[0] for t in tuples]))
second = np.array(sorted([t[1] for t in tuples]))

d = {}
for num in set(first):
    d[num] = np.count_nonzero(second == num)

res = 0
for num in first:
    res += num * d[num]

print(res)
