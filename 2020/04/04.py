import re

VALID_PARTS = set(
    [
        frozenset(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]),
        frozenset(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]),
    ]
)

with open("inputs/4.txt") as file:
    whole_file = file.read()
    passports = whole_file.split("\n\n")


def part_1():
    valid = 0
    for passport in passports:
        parts = set()
        fields = passport.split()
        for field in fields:
            parts.add(field.split(":")[0])
        if parts in VALID_PARTS:
            valid += 1
    return valid


def part_2():
    valid = 0
    for passport in passports:
        parts = {}
        fields = passport.split()
        for field in fields:
            part, value = field.split(":")
            parts[part] = value
        if set(parts.keys()) not in VALID_PARTS:
            continue
        if int(parts["byr"]) < 1920 or int(parts["byr"]) > 2002:
            continue
        if int(parts["iyr"]) < 2010 or int(parts["iyr"]) > 2020:
            continue
        if int(parts["eyr"]) < 2020 or int(parts["eyr"]) > 2030:
            continue
        unit = parts["hgt"][-2:]
        if unit != "in" and unit != "cm":
            continue
        height_value = int(parts["hgt"][:-2])
        if ((unit == "cm") and (height_value < 150 or height_value > 193)) or (
            (unit == "in") and (height_value < 59 or height_value > 76)
        ):
            continue
        if not re.search("^#[0-9a-f]{6}$", parts["hcl"]):
            continue
        if parts["ecl"] not in set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
            continue
        if not re.search("^[0-9]{9}$", parts["pid"]):
            continue
        valid += 1
    return valid


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
