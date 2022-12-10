DIRECTIONS = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
with open("inputs/9.txt") as file:
    lines = [line.strip().split(" ") for line in file]
    input_data = [(line[0], int(line[1])) for line in lines]


knots = [[0, 0] for _ in range(10)]
part_1_positions = set()
part_2_positions = set()
for direction, amount in input_data:
    x_move, y_move = DIRECTIONS[direction]
    for _ in range(amount):
        knots[0][0] += x_move
        knots[0][1] += y_move
        for index in range(1, len(knots)):
            knot_1 = knots[index - 1]
            knot_2 = knots[index]
            if (abs(knot_1[0] - knot_2[0]) > 1) or (abs(knot_1[1] - knot_2[1]) > 1):
                if knot_1[0] > knot_2[0]:
                    knot_2[0] += 1
                if knot_1[0] < knot_2[0]:
                    knot_2[0] -= 1
                if knot_1[1] > knot_2[1]:
                    knot_2[1] += 1
                if knot_1[1] < knot_2[1]:
                    knot_2[1] -= 1
        part_1_positions.add(tuple(knots[1]))
        part_2_positions.add(tuple(knots[-1]))
part_1 = len(part_1_positions)
part_2 = len(part_2_positions)

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
