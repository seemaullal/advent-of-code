part_1 = 0
part_2 = 0

def is_safe(report):
    decreasing = report[0] > report[1]
    increasing = report[0] < report[1]
    for level1, level2 in zip(report, report[1:]):
        if level1 > level2 and not decreasing:
            return False
        if level1 < level2 and not increasing:
            return False
        if abs(level1 - level2) < 1 or abs(level1 - level2) > 3:
            return False
    return True

reports = []
with open("inputs/02.txt", "r") as file:
    for line in file.read().splitlines():
        reports.append([int(level) for level in line.split()])

for report in reports:
    if is_safe(report):
        part_1 += 1
        part_2 += 1
    else:
        for i in range(len(report)):
            if is_safe(report[:i] + report[i+1:]):
                part_2 += 1
                break

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
