part_1 = 0
part_2 = 0


def can_reach_target(target, parts, is_part_2):
    if len(parts) == 1:
        return parts[0] == target
    if can_reach_target(target, [parts[0] + parts[1]] + parts[2:], is_part_2):
        return True
    if can_reach_target(target, [parts[0] * parts[1]] + parts[2:], is_part_2):
        return True
    if is_part_2 and can_reach_target(
        target, [int(str(parts[0]) + str(parts[1]))] + parts[2:], is_part_2
    ):
        return True
    return False


puzzle = []
with open("inputs/07.txt", "r") as file:
    for line in file.read().splitlines():
        [goal, parts] = line.split(": ")
        goal = int(goal)
        parts = [int(part) for part in parts.split(" ")]
        puzzle.append((goal, parts))

for goal, parts in puzzle:
    if can_reach_target(goal, parts, False):
        part_1 += goal
    if can_reach_target(goal, parts, True):
        part_2 += goal
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
