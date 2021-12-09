from collections import Counter
all_adapters = sorted([int(line.strip()) for line in open("day10_input.txt").readlines()] + [0])
all_adapters.append(max(all_adapters) + 3)

# part 1
adapter_difference_count = Counter()
last = None
for adapter in all_adapters:
    if last is not None:
        diff = adapter - last
        adapter_difference_count[diff] = adapter_difference_count[diff] + 1
    last = adapter
print('part 1', adapter_difference_count[1] * adapter_difference_count[3])

# part 2
counts = Counter({0: 1})
for current_index, adapter in enumerate(all_adapters):
    if current_index == len(all_adapters)-1:
        break
    second_index = current_index + 1
    to_check = all_adapters[second_index]
    while to_check <= adapter + 3 and second_index < len(all_adapters):
        counts[to_check] += counts[adapter]
        second_index += 1
        if second_index < len(all_adapters):
            to_check = all_adapters[second_index]
print('part 2', counts[all_adapters[-1]])