import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/18.txt"
with open(input_file) as file:
    lines = [line.strip() for line in file.readlines()]


class SnailfishInteger:
    def __init__(self, num):
        self.value = num

    def add_to_left(self, to_add):
        return SnailfishInteger(self + to_add)

    def add_to_right(self, to_add):
        return SnailfishInteger(self + to_add)

    def split(self):
        if self.value < 10:
            return (self, False)
        left = self.value // 2  # always round down
        right = -(-self.value // 2)  # always round up
        return (SnailfishPair(SnailfishInteger(left), SnailfishInteger(right)), True)

    def explode(self):
        return (self, None)

    def explode_recursive(self, depth=1):
        return self.explode()

    def __add__(self, to_add):
        if type(to_add) == SnailfishInteger:
            to_add = to_add.value
        return self.value + to_add

    def magnitude(self):
        return self.value

    # def __str__(self):
    #     return f"{self.value}"

    # def __repr__(self):
    #     return f"{self.value}"


class SnailfishPair:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def add_to_left(self, value):
        return SnailfishPair(self.left.add_to_left(value), self.right)

    def add_to_right(self, value):
        return SnailfishPair(self.left, self.right.add_to_right(value))

    def split(self):
        new_left, split_value = self.left.split()
        if split_value:
            return (SnailfishPair(new_left, self.right), True)
        new_right, split_value = self.right.split()
        if split_value:
            return (SnailfishPair(self.left, new_right), True)
        return (self, False)

    def explode(self):
        new_pair, parts = self.explode_recursive(1)
        if parts:
            return (new_pair, True)
        return (new_pair, False)

    def explode_recursive(self, current_depth):
        new_left, parts = self.left.explode_recursive(current_depth + 1)
        if parts is not None:
            left, right = parts
            return (SnailfishPair(new_left, self.right.add_to_left(right)), (left, 0))

        new_right, parts = self.right.explode_recursive(current_depth + 1)
        if parts is not None:
            left, right = parts
            return (SnailfishPair(self.left.add_to_right(left), new_right), (0, right))

        if current_depth > 4:
            return (
                SnailfishInteger(0),
                (SnailfishInteger(self.left).value, SnailfishInteger(self.right).value),
            )

        return (self, None)

    def reduce(self):
        exploded_part, is_exploded = self.explode()
        if is_exploded:
            return exploded_part.reduce()
        splitted, is_split = exploded_part.split()
        if is_split:
            return splitted.reduce()
        return self

    def __add__(self, to_add):
        return SnailfishPair(self, to_add).reduce()

    def __str__(self):
        return f"[{self.left}, {self.right}]"

    def __repr__(self):
        return f"[{self.left}, {self.right}]"

    def magnitude(self):
        return self.left.magnitude() * 3 + self.right.magnitude() * 2


def parse_line(line: str, bracket_num=0):
    if line[bracket_num].isdigit():
        return (SnailfishInteger(int(line[bracket_num])), bracket_num + 1)
    left, brackets_left = parse_line(line, bracket_num + 1)
    right, brackets_right = parse_line(line, brackets_left + 1)
    return (SnailfishPair(left, right), brackets_right + 1)


def part_1():
    parsed = [parse_line(line)[0] for line in lines]
    return sum(parsed, parsed[0]).magnitude()


def part_2():
    parsed = [parse_line(line)[0] for line in lines]
    max_magnitude = float("-inf")
    for i in range(len(parsed)):
        for j in range(i + 1, len(parsed)):
            max_magnitude = max(max_magnitude, (parsed[i] + parsed[j]).magnitude())
    return max_magnitude


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
