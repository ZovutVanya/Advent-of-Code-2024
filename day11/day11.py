# from time import time
# from itertools import groupby
from functools import cache

with open("input.txt", "r") as f:
    nums = f.readline().split()


@cache
def count_stones(num: str, depth: int):
    if depth == 0:
        return 1
    if num == "0" or num == "":
        return count_stones("1", depth - 1)
    q, r = divmod(len(num), 2)
    if r != 0:
        return count_stones(str(int(num) * 2024), depth - 1)
    return count_stones(num[:q], depth - 1) + count_stones(
        num[q:].lstrip("0"), depth - 1)


print(sum(count_stones(n, 25) for n in nums))
print(sum(count_stones(n, 75) for n in nums))

# subs = {"0": "1", "1": "2024"}
#
#
# i = 0
# while i < 75:
#     start = time()
#     # nums = [list(g) for k, g in groupby(sorted(nums, key=len), key=len)]
#     # evens = [row for col in nums[1::2] for row in col]
#     # odds = [row for col in nums[0::2] for row in col]
#     # new_evens = []
#     # new_odds = []
#     # for i, even in enumerate(evens):
#     #     try:
#     #         new_evens.append(subs[even])
#     #     except Exception:
#     #         even_half = len(even) // 2
#     #         halves = (even[:even_half], even[even_half:])
#     #         new_evens.append(halves)
#     #         subs[even] = halves
#     # for i, odd in enumerate(odds):
#     #     try:
#     #         new_odds.append(subs[odd])
#     #     except Exception:
#     #         new_num = str(2024 * int(odd))
#     #         new_odds.append(new_num)
#     #         subs[odd] = new_num
#     # nums = new_odds + [row for col in new_evens for row in col]
#     new_nums = []
#     for num in nums:
#         try:
#             new_nums.append(subs[num])
#         except Exception:
#             q, r = divmod(len(num), 2)
#             if r == 0:
#                 new_nums.append(num[:q])
#                 new_nums.append(str(int(num[q:])))
#             else:
#                 new_num = str(2024*int(num))
#                 new_nums.append(new_num)
#                 subs[num] = new_num
#     i += 1
#     # print(nums)
#     # print(evens)
#     # print(odds)
#     nums = new_nums
#     print(time() - start)
#
# print(len(nums))
