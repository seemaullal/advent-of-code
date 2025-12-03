part_1 = 0
part_2 = 0

with open("inputs/input.txt", "r") as file:
    current = 50
    for line in file.read().splitlines():
        rotation = line[0]
        distance = int(line[1:])
        for num in range(distance):
            if rotation == "L":
                current -= 1
            else:
                current += 1
            current = current % 100
            if current == 0:
                part_2 += 1
        # if rotation == "L":
        #     current = (current - distance + 100) % 100
        # else:
        #     current = (current + distance) % 100
        # if current == 0:
        #     part_1 += 1


print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
