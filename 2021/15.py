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


def find_shortest_path(graph):
    row_num = len(graph)
    col_num = len(graph[0])
    to_visit = [(0, (0, 0))]
    distances = {(i, j): float("inf") for j in range(col_num) for i in range(row_num)}
    while True:
        current_distance, coordinates = heappop(to_visit)
        current_row, current_col = coordinates
        if current_row == row_num - 1 and current_col == col_num - 1:
            return current_distance
        possible_neighbors = [
            (current_row - 1, current_col),
            (current_row + 1, current_col),
            (current_row, current_col - 1),
            (current_row, current_col + 1),
        ]
        for neighbor_row, neighbor_col in possible_neighbors:
            if neighbor_row < 0 or neighbor_col < 0 or neighbor_row >= row_num or neighbor_col >= col_num:
                continue
            potential_distance = current_distance + graph[neighbor_row][neighbor_col]
            if potential_distance < distances[(neighbor_row, neighbor_col)]:
                distances[(neighbor_row, neighbor_col)] = potential_distance
                heappush(to_visit, (potential_distance, ((neighbor_row, neighbor_col))))


def part_1():
    return find_shortest_path(risk_levels)


def part_2():
    larger_map = get_larger_map()
    return find_shortest_path(larger_map)


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
