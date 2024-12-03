with open("input.txt", "r") as f:
    lines = f.readlines()

reports = [[int(level) for level in levels.strip().split()]
           for levels in lines]

res = 0

for report in reports:
    report_versions = []
    for i in range(len(report) + 1):
        report_versions.append([el for j, el in enumerate(report) if j != i])
    flag = len(report_versions)
    for r in report_versions:
        if r == sorted(r) or r == sorted(r, reverse=True):
            for f, s in zip(r, r[1:]):
                if not (1 <= abs(f - s) <= 3):
                    flag -= 1
                    break
        else:
            flag -= 1
            continue
    res += int(flag > 0)

print(res)
