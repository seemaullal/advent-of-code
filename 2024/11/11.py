from collections import Counter


with open("inputs/11.txt", "r") as file:
    for line in file.read().splitlines():
        stones = [stone for stone in line.split()]


def calculate(n):
    stone_count = Counter(stones)
    for _ in range(n):
        updated_stone_count = Counter()
        for stone, count in stone_count.items():
            if stone == '0':
                updated_stone_count['1'] += count
            elif len(stone) % 2 == 0:
                # convert to int to remove leading zeros
                updated_stone_count[
                   str(int(stone[: len(stone) // 2]))
                ] += count
                updated_stone_count[
                   str(int(stone[len(stone) // 2 :]))
                ] += count
            else:
                updated_stone_count[str(int(stone) * 2024)] += count
        stone_count = updated_stone_count
    return stone_count.total()


part_1 = calculate(25)
part_2 = calculate(75)


print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
