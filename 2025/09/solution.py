from pathlib import Path

def solve():
    coordinates = [tuple(int(num) for num in row.split(',')) for row in Path("inputs/input.txt").read_text().strip().splitlines()]
    coord_set = set(coordinates)
    
    max_area = 0
    
    for i in range(len(coordinates)):
        x1, y1 = coordinates[i]
        for j in range(i + 1, len(coordinates)):
            x2, y2 = coordinates[j]
            
            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            max_area = max(max_area, width * height)
    
    print(f"Part 1: {max_area}")

   


if __name__ == "__main__":
    solve()
