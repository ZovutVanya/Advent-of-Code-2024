import re
import numpy as np
from numpy.linalg import solve

with open("input.txt", "r") as f:
    machine_info = f.read().strip().split('\n\n')

CORRECTION = 10000000000000


def cost(a, b):
    return 3 * a + b


min_token_count = 0
min_token_count_corr = 0
for info in machine_info:
    button_a, button_b, prize = info.split('\n')

    button_a = re.findall(r'(\d+)\D*(\d+)', button_a)[0]
    button_b = re.findall(r'(\d+)\D*(\d+)', button_b)[0]
    prize = re.findall(r'(\d+)\D*(\d+)', prize)[0]

    button_a = np.int64(button_a)
    button_b = np.int64(button_b)
    prize = np.int64(prize)
    prize_w_corr = prize + CORRECTION

    AB = np.column_stack((button_a, button_b))

    solution = np.rint(solve(AB, prize))
    if np.all(AB @ solution == prize):
        min_token_count += cost(*solution)

    solution2 = np.rint(solve(AB, prize_w_corr))
    if np.all(AB @ solution2 == prize_w_corr):
        min_token_count_corr += cost(*solution2)

print(f'Part 1: {min_token_count}')
print(f'Part 2: {min_token_count_corr}')
