DIRECTIONS = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
with open("inputs/9.txt") as file:
    lines = [line.strip().split(" ") for line in file]
    input_data = [(line[0], int(line[1])) for line in lines]

knots = [[0, 0] for _ in range(10)]
part_1_positions, part_2_positions = set(), set()
for direction, amount in input_data:
    x_move, y_move = DIRECTIONS[direction]
    for _ in range(amount):
        knots[0] = [knots[0][0] + x_move, knots[0][1] + y_move]
        for index in range(1, len(knots)):
            knot_1_x, knot_1_y, knot_2_x, knot_2_y = knots[index - 1] + knots[index]
            if (abs(knot_1_x - knot_2_x) > 1) or (abs(knot_1_y - knot_2_y) > 1):
                knots[index][0] += int(knot_1_x > knot_2_x) - int(knot_1_x < knot_2_x)
                knots[index][1] += int(knot_1_y > knot_2_y) - int(knot_1_y < knot_2_y)
        part_1_positions.add(tuple(knots[1]))
        part_2_positions.add(tuple(knots[-1]))

print(f"Part 1: {len(part_1_positions)}")
print(f"Part 2: {len(part_2_positions)}")
