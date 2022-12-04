import re

file = open('day_4_input.txt')
whole_file = file.read()
passports = whole_file.split('\n\n')
valid = 0
valid_parts = [
    set(['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']),
    set(['byr','iyr','eyr','hgt','hcl','ecl','pid'])
]

for passport in passports:
    parts = {}
    fields = passport.split()
    for field in fields:
        part, value = field.split(':')
        parts[part] = value
    if set(parts.keys()) not in valid_parts:
        continue
    if int(parts['byr']) < 1920 or int(parts['byr']) > 2002:
        continue
    if int(parts['iyr']) < 2010 or int(parts['iyr']) > 2020:
        continue
    if int(parts['eyr']) < 2020 or int(parts['eyr']) > 2030:
        continue
    unit = parts['hgt'][-2:]
    if unit != 'in' and unit != 'cm':
        continue
    height_value = int(parts['hgt'][:-2])
    if ((unit == 'cm') and (height_value < 150 or height_value > 193)) or ((unit == 'in') and (height_value < 59 or height_value > 76)):
        continue
    if not re.search('^#[0-9a-f]{6}$', parts['hcl']):
        continue
    if parts['ecl'] not in set(['amb','blu','brn','gry','grn','hzl', 'oth']):
        continue
    if not re.search('^[0-9]{9}$', parts['pid']):
        continue
    valid +=1
print(valid)
