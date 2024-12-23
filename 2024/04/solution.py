with open("inputs/input.txt", "r") as file:
    word_search = [list(line) for line in file.read().splitlines()]

NUM_ROWS = len(word_search)
NUM_COLS = len(word_search[0])

DIRECTIONS = [
    (0, 1),  # right
    (0, -1),  # left
    (1, 0),  # down
    (-1, 0),  # up
    (1, 1),  # diagonal down-right
    (1, -1),  # diagonal down-left
    (-1, -1),  # diagonal up-left
    (-1, 1),  # diagonal up-right
]
MAS_PATTERNS = [
    ("M", "S", "M", "S"),
    ("M", "M", "S", "S"),
    ("S", "S", "M", "M"),
    ("S", "M", "S", "M"),
]


def is_valid_position(row, col):
    return 0 <= row < NUM_ROWS and 0 <= col < NUM_COLS


def check_xmas_pattern(start_row, start_col, row_delta, col_delta):
    for index, letter in enumerate("XMAS"):
        row = start_row + (row_delta * index)
        col = start_col + (col_delta * index)

        if not is_valid_position(row, col) or word_search[row][col] != letter:
            return False
    return True


def check_mas_square_pattern(row, col, pattern):
    if not is_valid_position(row + 2, col + 2):
        return False

    # Center must always be 'A'
    if word_search[row + 1][col + 1] != "A":
        return False

    return (
        word_search[row][col] == pattern[0]  # top-left
        and word_search[row][col + 2] == pattern[1]  # top-right
        and word_search[row + 2][col] == pattern[2]  # bottom-left
        and word_search[row + 2][col + 2] == pattern[3]  # bottom-right
    )


part_1 = 0
part_2 = 0
for row_number in range(NUM_ROWS):
    for column_number in range(NUM_COLS):
        for row_delta, col_delta in DIRECTIONS:
            if check_xmas_pattern(row_number, column_number, row_delta, col_delta):
                part_1 += 1

        for pattern in MAS_PATTERNS:
            if check_mas_square_pattern(row_number, column_number, pattern):
                part_2 += 1

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
