import re
with open("input.txt", "r") as f:
    lines = f.readlines()

line = "".join(lines)


def mul(x: int, y: int) -> int:
    return x*y


muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)


res = 0
flag = True
for fun in muls:
    if fun == "don't()":
        flag = False
        continue
    if fun == "do()":
        flag = True
        continue
    if flag:
        res += eval(fun)

print(res)
