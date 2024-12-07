with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

break_idx = lines.index("")

rules = [
    tuple(int(string) for string in rule.split("|")) for rule in lines[0:break_idx]
]
pages_lines = [
    [int(string) for string in pages.split(",")]
    for pages in lines[(break_idx + 1):]
]

correct_updates_middles = []
incorrect_updates = []
for pages_line in pages_lines:
    flag = True
    for i, page in enumerate(pages_line):
        if set(
            [tuple([page, other_page]) for other_page in pages_line[(i + 1):]]
        ).issubset(rules):
            continue
        else:
            flag = False
            break
    if flag:
        correct_updates_middles.append(pages_line[len(pages_line) // 2])
    else:
        incorrect_updates.append(pages_line)


print(sum(correct_updates_middles))


def check_correctness(update):
    flag = True
    for i, page in enumerate(update):
        if set(
            [tuple([page, other_page]) for other_page in update[(i + 1):]]
        ).issubset(rules):
            continue
        else:
            flag = False
            break
    return flag


for update in incorrect_updates:
    while not check_correctness(update):
        for i, (f, s) in enumerate(zip(update, update[1:])):
            if tuple([s, f]) in rules:
                update[i], update[i+1] = update[i+1], update[i]

print(sum([update[len(update)//2] for update in incorrect_updates]))
