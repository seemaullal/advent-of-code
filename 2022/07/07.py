from collections import defaultdict

with open("inputs/7.txt") as file:
    commands = [line.strip().split(" ") for line in file]

directories = defaultdict(list)

index = 0
current_directory = ""
while index < len(commands):
    command = commands[index]
    if command[0] == "$":
        if command[1] == "cd":
            if command[2].startswith("/"):
                current_directory = command[2][1:]
            elif command[2] == "..":
                current_directory = (
                    current_directory[: current_directory.rfind("/")] or "/"
                )
            else:
                if not current_directory.endswith("/"):
                    current_directory += "/"
                current_directory += f"{command[2]}"
            index += 1
        if command[1] == "ls":
            index += 1
            while index < len(commands) and commands[index][0] != "$":
                part_1, part_2 = commands[index]
                if part_1 == "dir":
                    directories[current_directory].append(
                        f"{current_directory}/{part_2}"
                    )
                else:
                    directories[current_directory].append(int(part_1))
                index += 1

directory_sizes = {}


def part_1():
    result = 0
    for directory in directories:
        size = 0
        to_visit = directories[directory][:]
        while to_visit:
            current = to_visit.pop(-1)
            if isinstance(current, int):
                size += current
            else:
                to_visit.extend(directories.get(current, []))
        if size <= 100_000:
            result += size
        directory_sizes[directory] = size
    return result


def part_2():
    total_size = 70_000_000
    space_needed = 30_000_000
    currently_free = total_size - directory_sizes[""]
    for size in sorted(directory_sizes.values()):
        if currently_free + size > space_needed:
            return size


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
