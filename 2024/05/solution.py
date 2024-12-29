from collections import defaultdict

part_1 = 0
part_2 = 0

with open("inputs/05.txt", "r") as file:
    ordering_rules, pages = file.read().strip().split("\n\n")

ordering_rules = [
    (int(rule[0]), int(rule[1]))
    for rule in [rule.split("|") for rule in ordering_rules.split("\n")]
]

pages_before = defaultdict(set)
pages_after = defaultdict(set)
for first, second in ordering_rules:
    pages_before[second].add(first)
    pages_after[first].add(second)
for page in pages.split("\n"):
    order = [int(x) for x in page.split(",")]
    valid = True
    for index_1, page_1 in enumerate(order):
        for index_2, page_2 in enumerate(order):
            if index_1 < index_2 and page_2 in pages_before[page_1]:
                valid = False
    if valid:
        part_1 += order[len(order) // 2]
    else:
        valid_pages = []
        to_visit = []
        intersecting_page_number = {
            page: len(pages_before[page] & set(order)) for page in order
        }
        for page in order:
            if intersecting_page_number[page] == 0:
                to_visit.append(page)
        while to_visit:
            page = to_visit.pop()
            valid_pages.append(page)
            for other_page in pages_after[page]:
                if other_page in intersecting_page_number:
                    intersecting_page_number[other_page] -= 1
                    if intersecting_page_number[other_page] == 0:
                        to_visit.append(other_page)
        part_2 += valid_pages[len(valid_pages) // 2]


print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
