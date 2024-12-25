with open("input.txt") as f:
    stuff = [kl.split("\n") for kl in f.read().split("\n\n")]

del stuff[-1][-1]


def get_heights(smthn):
    transposed = [[row[i] for row in smthn] for i in range(rowlen)]
    return [col.count("#") - 1 for col in transposed]


locks = []
keys = []
rowlen = len(stuff[0][0])

for smthn in stuff:
    if smthn[0] == "#####":
        locks.append(get_heights(smthn))
    else:
        keys.append(get_heights(smthn))


counter = 0
for lock in locks:
    for key in keys:
        flag = True
        for i in range(rowlen):
            if lock[i] + key[i] >= 6:
                flag = False
                break
        if flag:
            counter += 1
            # break

print(counter)
