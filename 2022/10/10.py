class Day10:
    def __init__(self):
        with open("inputs/10.txt") as file:
            self.instructions = [
                command.split() for command in file.read().splitlines()
            ]
        self.part_1 = self.cycle_number = 0
        self.x = 1
        self.pixels = [["" for _ in range(40)] for _ in range(6)]
        self.is_solved = False
        self.solve()

    def strength_increase(self):
        return self.cycle_number * self.x if self.cycle_number % 40 == 20 else 0

    def update_pixels(self):
        row_number = self.cycle_number // 40
        col_number = self.cycle_number % 40
        self.pixels[row_number][col_number] = (
            "█" if abs(self.x - col_number) <= 1 else " "
        )
        self.cycle_number += 1
        self.part_1 += self.strength_increase()

    def solve(self):
        if not self.is_solved:
            for instruction in self.instructions:
                self.step()
                if instruction[0] == "addx":
                    self.step()
                    self.x += int(instruction[1])
            self.is_solved = True

    def print_part_2(self):
        print(f"Part 2:")
        print("\n".join(["".join(row) for row in self.pixels]))


day_10 = Day10()
print(f"Part 1: {day_10.part_1}")
day_10.print_part_2()
