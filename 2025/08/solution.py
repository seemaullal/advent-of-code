from pathlib import Path
from collections import Counter


def find(u, parent):
    while parent[u] != u:
        parent[u] = parent[parent[u]]
        u = parent[u]
    return u

def union(u, v, parent, size):
    pu, pv = find(u, parent), find(v, parent)
    if pu == pv:
        return False
    if size[pu] < size[pv]:
        pu, pv = pv, pu
    parent[pv] = pu
    size[pu] += size[pv]
    return True

def solve():
    boxes = [tuple(int(num) for num in row.split(',')) for row in Path("inputs/input.txt").read_text().strip().splitlines()]
    
    n = len(boxes)

    edges = []
    for i in range(n):
        xi, yi, zi = boxes[i]
        for j in range(i+1, n):
            xj, yj, zj = boxes[j]
            dist = ((xi-xj)**2 + (yi-yj)**2 + (zi-zj)**2)**0.5
            edges.append((dist, i, j))

    # Sort all edges by distance
    edges.sort()

    parent1 = list(range(n))
    size1 = [1] * n
    for dist, u, v in edges[:1000]:
        union(u, v, parent1, size1)

    comp_size1 = Counter()
    for i in range(n):
        comp_size1[find(i, parent1)] += 1

    sorted_sizes = sorted(comp_size1.values())
    part1 = sorted_sizes[-3] * sorted_sizes[-2] * sorted_sizes[-1]

    parent2 = list(range(n))
    size2 = [1] * n
    comps = n
    last_edge = None
    for _, u, v in edges:
        if union(u, v, parent2, size2):
            comps -= 1
            if comps == 1:
                last_edge = (u, v)
                break
                
    part2 = boxes[last_edge[0]][0] * boxes[last_edge[1]][0]

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

   


if __name__ == "__main__":
    solve()
