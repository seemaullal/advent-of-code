import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/18.txt"
with open(input_file) as file:
    lines = [line.strip() for line in file.readlines()]


class SnailfishSingle:
    def __init__(self, num):
        self.value = num

    def add_to_left(self, to_add):
        return SnailfishSingle(self + to_add)

    def add_to_right(self, to_add):
        return SnailfishSingle(self + to_add)

    def split(self):
        if self.value < 10:
            return (self, False)
        left = self.value // 2  # always round down
        right = -(-self.value // 2)  # always round up
        return (SnailfishMultiple(SnailfishSingle(left), SnailfishSingle(right)), True)

    def explode(self):
        return (self, None)

    def explode_recursive(self, depth=1):
        return self.explode()

    def __add__(self, to_add):
        if isinstance(to_add, SnailfishSingle):
            to_add = to_add.value
        return self.value + to_add

    def magnitude(self):
        return self.value

    def __repr__(self):
        return f"{self.value}"

    __str__ = __repr__


class SnailfishMultiple:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def add_to_left(self, value):
        return SnailfishMultiple(self.left.add_to_left(value), self.right)

    def add_to_right(self, value):
        return SnailfishMultiple(self.left, self.right.add_to_right(value))

    def split(self):
        new_left, split_value = self.left.split()
        if split_value:
            return (SnailfishMultiple(new_left, self.right), True)
        new_right, split_value = self.right.split()
        if split_value:
            return (SnailfishMultiple(self.left, new_right), True)
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
            return (SnailfishMultiple(new_left, self.right.add_to_left(right)), (left, 0))

        new_right, parts = self.right.explode_recursive(current_depth + 1)
        if parts is not None:
            left, right = parts
            return (SnailfishMultiple(self.left.add_to_right(left), new_right), (0, right))

        if current_depth > 4:
            return (
                SnailfishSingle(0),
                (SnailfishSingle(self.left).value, SnailfishSingle(self.right).value),
            )

        return (self, None)

    def reduce(self):
        exploded_part, is_exploded = self.explode()
        if is_exploded:
            return exploded_part.reduce()
        split_part, is_split = exploded_part.split()
        if is_split:
            return split_part.reduce()
        return self

    def __add__(self, to_add):
        return SnailfishMultiple(self, to_add).reduce()

    def __repr__(self):
        return f"[{self.left}, {self.right}]"

    __str__ = __repr__

    def magnitude(self):
        return self.left.magnitude() * 3 + self.right.magnitude() * 2


def parse_line(curr):
    if isinstance(curr, int):
        return SnailfishSingle(curr)
    left = parse_line(curr[0])
    right = parse_line(curr[1])
    return SnailfishMultiple(left, right)


def part_1():
    parsed = [parse_line(eval(line)) for line in lines]
    return sum(parsed, parsed[0]).magnitude()


def part_2():
    parsed = [parse_line(eval(line)) for line in lines]
    max_magnitude = float("-inf")
    for i in range(len(parsed)):
        for j in range(i + 1, len(parsed)):
            max_magnitude = max(max_magnitude, (parsed[i] + parsed[j]).magnitude())
    return max_magnitude


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
