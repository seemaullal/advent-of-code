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
    parent = list(range(n))
    size = [1] * n


    edges = []
    for i in range(n):
        xi, yi, zi = boxes[i]
        for j in range(i+1, n):
            xj, yj, zj = boxes[j]
            dist = ((xi-xj)**2 + (yi-yj)**2 + (zi-zj)**2)**0.5
            edges.append((dist, i, j))

    # Sort all edges by distance
    edges.sort()
    # Apply the first 1000 shortest connections, even if they don't merge components
    for dist, u, v in edges[:1000]:
        union(u, v, parent, size)

    comp_size = Counter()
    for i in range(n):
        comp_size[find(i, parent)] += 1

    sorted_sizes = sorted(comp_size.values())
    part1 = sorted_sizes[-3] * sorted_sizes[-2] * sorted_sizes[-1]

    print(f"Part 1: {part1}")

   


if __name__ == "__main__":
    solve()
