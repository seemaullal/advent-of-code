DIRECTIONS = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
with open("inputs/9.txt") as file:
    lines = [line.strip().split(" ") for line in file]
    input_data = [(line[0], int(line[1])) for line in lines]


def part_1():
    visited = set()
    head = [0, 0]
    tail = [0, 0]
    for direction, amount in input_data:
        x_move, y_move = DIRECTIONS[direction]
        for _ in range(amount):
            head[0] += x_move
            head[1] += y_move
            if (abs(head[0] - tail[0]) > 1) or (abs(head[1] - tail[1]) > 1):
                if head[0] - tail[0] > 0:
                    tail[0] += 1
                if head[0] - tail[0] < 0:
                    tail[0] -= 1
                if head[1] - tail[1] > 0:
                    tail[1] += 1
                if head[1] - tail[1] < 0:
                    tail[1] -= 1
            visited.add((tail[0], tail[1]))
    return len(visited)


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
