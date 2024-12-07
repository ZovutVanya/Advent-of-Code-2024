from itertools import product

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# for part one remove ||
ops = ("+", "*", "||")


def gen_combos(nums: list[str]):
    combos = product(ops, repeat=len(nums) - 1)

    results = []
    for combo in combos:
        result = [nums[0]]
        for i in range(len(nums) - 1):
            result.append(combo[i])
            result.append(nums[i + 1])
        results.append(result)

    return results


def eval_left2right(ex: list[str]):
    if len(ex) == 1:
        return int(ex[0])
    else:
        n1, op, n2 = ex[0], ex[1], ex[2]
        ex = ex[3:]
        if op == "||":
            num = n1+n2
        else:
            num = str(eval("".join([n1, op, n2])))
        ex.insert(0, num)
        return eval_left2right(ex)


res = 0
for line in lines:
    left, right = line.split(": ")
    right = right.split(" ")
    left = int(left)

    combos = gen_combos(right)
    for combo in combos:
        if eval_left2right(combo) == left:
            res += left
            break

print(res)
