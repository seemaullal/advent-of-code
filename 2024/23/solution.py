from collections import defaultdict

connections = defaultdict(set)
with open("inputs/input.txt", "r") as file:
    for line in file.read().splitlines():
        computer_1, computer_2 = line.split("-")
        connections[computer_1].add(computer_2)
        connections[computer_2].add(computer_1)

graph_nodes = list(connections.keys())
part_1 = 0
for index_1,computer_1 in enumerate(graph_nodes):
    for index_2 in range(index_1+1, len(graph_nodes)):
        for index_3 in range(index_2+1, len(graph_nodes)):
            computer_2 = graph_nodes[index_2]
            computer_3 = graph_nodes[index_3]
            if computer_1 in connections[computer_2] and computer_1 in connections[computer_3] and computer_2 in connections[computer_3]:
                if computer_1.startswith('t') or computer_2.startswith('t') or computer_3.startswith('t'):
                    part_1 += 1

best = None
for node in graph_nodes:
    node_connections = connections[node]
    connections_and_node = set(node_connections) | set((node,))
    possibilities = [connections_and_node]

    for connection in node_connections:
        c = set(connections[connection]) | set((connection,))
        valid_trials = []
        for possibility in possibilities:
            intersection = c & possibility
            if intersection:
                valid_trials.append(intersection)
            valid_trials.append(possibility - set((connection,)))
        possibilities = valid_trials
    for possibility in possibilities:
        if best is None or len(possibility) > len(best):
            best = possibility

print(f"Part 1: {part_1}")
print(f"Part 2: {','.join(sorted(best))}")
