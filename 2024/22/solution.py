from collections import Counter

with open("inputs/input.txt", "r") as file:
    nums = [int(num) for num in file.read().splitlines()]


def mix(num1, num2):
    return num1 ^ num2


def prune(num):
    return num % 16777216


counts = Counter()
part_1 = 0
for num in nums:
    seen = set()
    current_price_sequence = ()
    secret_number = num
    for _ in range(2000):
        previous_ones_digit = secret_number % 10
        secret_number = prune(mix(secret_number, secret_number * 64))
        secret_number = prune(mix(secret_number, secret_number // 32))
        secret_number = prune(mix(secret_number, secret_number * 2048))
        new_ones_digit = secret_number % 10
        current_price_sequence = current_price_sequence[-3:] + (
            new_ones_digit - previous_ones_digit,
        )
        if current_price_sequence not in seen:
            seen.add(current_price_sequence)
            counts[current_price_sequence] += new_ones_digit
    part_1 += secret_number

print(f"Part 1: {part_1}")
print(f"Part 2: {counts.most_common()[0][1]}")
