with open("inputs/1.txt") as file:
    entries = [int(entry) for entry in file.readlines()]


def part_1():
    seen = set()
    for entry in entries:
        if 2020 - entry in seen:
            return entry * (2020 - entry)
        seen.add(entry)


def part_2():
    entries.sort()
    for i in range(len(entries) - 2):
        left = i + 1
        right = len(entries)-1
        while (left < right):
            if(entries[i] + entries[left] + entries[right] == 2020):
                return entries[i] * entries[left] * entries[right]
            elif (entries[i] + entries[left] + entries[right] < 2020):
                left += 1
            else:
                right -= 1
    return "Uh oh! No matching entries found 😱"


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
