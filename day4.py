with open("inputs/day4.txt") as file:
    nums = [int(num.strip()) for num in file.readline().split(",")]
    boards = []
    for board in file.read().split("\n\n"):
        current_board = []
        for line in board.strip().split("\n"):
            current_board.append([int(num) for num in line.strip().split(" ") if num != ""])
        boards.append(current_board)


def check_winner(board):
    for row in board:
        if set(row) == {"X"}:
            return True
    for col_num in range(len(board[0])):
        only_x = True
        for row in board:
            if row[col_num] != "X":
                only_x = False
        if only_x:
            return True
    return False


def calculate_score(board, current_called_number):
    sum_of_non_called = 0
    for row in board:
        for num in row:
            if num != "X":
                sum_of_non_called += num
    return sum_of_non_called * current_called_number


def mark_boards(boards_to_mark, current_number):
    for board in boards_to_mark:
        for row in board:
            for index, num in enumerate(row):
                if num == current_number:
                    row[index] = "X"


def part_1():
    for current_called_number in nums:
        mark_boards(boards, current_called_number)
        for board in boards:
            if check_winner(board):
                return calculate_score(board, current_called_number)


def part_2():
    current_boards = boards[:]
    for current_called_number in nums:
        mark_boards(boards, current_called_number)
        boards_to_keep_playing = []
        for board in current_boards:
            if check_winner(board):
                if len(current_boards) == 1:
                    return calculate_score(board, current_called_number)
            else:
                boards_to_keep_playing.append(board)
        current_boards = boards_to_keep_playing


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
