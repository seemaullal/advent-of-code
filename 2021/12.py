import sys
from collections import defaultdict, deque

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/12.txt"
graph = defaultdict(set)
with open(input_file) as file:
    for line in file:
        first, second = line.strip().split("-")
        graph[first].add(second)
        graph[second].add(first)


def part_1():
    # store node name and set of small nodes we have seen
    current = ("start", {"start"})
    paths = 0
    to_visit = deque([current])
    while to_visit:
        node_name, small_visited = to_visit.popleft()
        if node_name == "end":
            paths += 1
            continue
        for dest in graph[node_name]:
            if dest not in small_visited:
                updated_small = set(small_visited)
                if dest.islower():
                    updated_small.add(dest)
                to_visit.append((dest, updated_small))
    return paths


def part_2():
    # store node name, small nodes seen, and if a small node was visited twice
    current = ("start", {"start"}, False)
    paths = 0
    to_visit = deque([current])
    while to_visit:
        node_name, small_visited, small_visited_twice = to_visit.popleft()
        if node_name == "end":
            paths += 1
        else:
            for dest in graph[node_name]:
                if dest not in small_visited:
                    updated_small = set(small_visited)
                    if dest.islower():
                        updated_small.add(dest)
                    to_visit.append((dest, updated_small, small_visited_twice))
                elif not small_visited_twice and dest not in {"start", "end"}:
                    to_visit.append((dest, small_visited, True))
    return paths


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
