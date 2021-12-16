import sys
from heapq import heappush, heappop

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/15.txt"
with open(input_file) as file:
    risk_levels = [list(map(int, list(line.strip()))) for line in file.readlines()]

ROW_NUM = len(risk_levels)
COL_NUM = len(risk_levels[0])
LARGER_MAP_ROWS = ROW_NUM * 5
LARGER_MAP_COLS = COL_NUM * 5


def get_larger_map():
    larger_map = [[None for _ in range(LARGER_MAP_COLS)] for _ in range(LARGER_MAP_ROWS)]
    for i in range(5 * ROW_NUM):
        for j in range(5 * COL_NUM):
            current = risk_levels[i % ROW_NUM][j % COL_NUM] + i // ROW_NUM + j // COL_NUM
            current = current % 9 if current > 9 else current
            larger_map[i][j] = current
    return larger_map


def part_1():
    distances = {(row, col): float("inf") for row in range(ROW_NUM) for col in range(COL_NUM)}
    to_visit_priority_queue = []
    heappush(to_visit_priority_queue, (0, (0, 0)))
    while True:
        current_distance, current_coordinates = heappop(to_visit_priority_queue)
        current_row, current_col = current_coordinates
        neighbors = []
        if current_row == ROW_NUM - 1 and current_col == COL_NUM - 1:
            return current_distance
        if current_row != ROW_NUM - 1:
            neighbors.append((current_row + 1, current_col))
        if current_col != COL_NUM - 1:
            neighbors.append((current_row, current_col + 1))
        for neighbor_row, neighbor_col in neighbors:
            tentative_risk_level = current_distance + risk_levels[neighbor_row][neighbor_col]
            if tentative_risk_level < distances[(neighbor_row, neighbor_col)]:
                distances[(neighbor_row, neighbor_col)] = tentative_risk_level
                heappush(to_visit_priority_queue, (tentative_risk_level, (neighbor_row, neighbor_col)))


def part_2():
    larger_map = get_larger_map()
    distances = {(x, y): float("inf") for x in range(LARGER_MAP_ROWS) for y in range(LARGER_MAP_COLS)}
    distances[(0, 0)] = 0
    pq = [(0, (0, 0))]
    while True:
        current_distance, current_coordinate = heappop(pq)
        current_row, current_col = current_coordinate
        if current_row == LARGER_MAP_ROWS - 1 and current_col == LARGER_MAP_COLS - 1:
            return current_distance
        neighbors = []
        if current_row != 0:
            neighbors.append((current_row - 1, current_col))
        if current_col != 0:
            neighbors.append((current_row, current_col - 1))
        if current_row != LARGER_MAP_ROWS - 1:
            neighbors.append((current_row + 1, current_col))
        if current_col != LARGER_MAP_COLS - 1:
            neighbors.append((current_row, current_col + 1))
        for n_x, n_y in neighbors:
            potential_distance = current_distance + larger_map[n_x][n_y]
            if potential_distance < distances[(n_x, n_y)]:
                distances[(n_x, n_y)] = potential_distance
                heappush(pq, (potential_distance, (n_x, n_y)))


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
