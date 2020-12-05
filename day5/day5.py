def binary_search_based_on_sequence(low, high, sequence, first_half_char):
    for char in sequence:
        midpoint = low + (high-low)//2
        if char == first_half_char:
            high = midpoint
        else:
            low = midpoint + 1
    return low if sequence[-1] == first_half_char else high

def compute_seat_id(boarding_pass_sequence):
    row_sequence = boarding_pass_sequence[:-3]
    col_sequence = boarding_pass_sequence[-3:]
    row_number = binary_search_based_on_sequence(0, 127, row_sequence, 'F')
    col_number = binary_search_based_on_sequence(0, 7, col_sequence, 'L')
    return row_number * 8 + col_number

# Needed for both parts
file = open('day5_input.txt')
boarding_passes = [line.strip() for line in file.readlines()]
all_seat_ids = set()
for boarding_pass_sequence in boarding_passes:
    all_seat_ids.add(compute_seat_id(boarding_pass_sequence))

# Part 1
print('part 1', max(all_seat_ids))

# Part 2
all_possible_seats = set(list(range(1, 127 * 8)))
missing_seats = all_possible_seats - all_seat_ids
for seat_id in missing_seats:
    if seat_id - 1 in all_seat_ids and seat_id + 1 in all_seat_ids:
        print('part 2', seat_id)