from pathlib import Path
from collections import defaultdict
import re


def solve():
    claims = Path("inputs/input.txt").read_text().strip().splitlines()
    part_1 = 0
    coordinate_claim_ids = defaultdict(set)
    all_claim_ids = set()

    for claim in claims:
        claim_id, left, top, width, height = map(int, re.findall(r"\d+", claim))
        all_claim_ids.add(claim_id)

        for x in range(left, left + width):
            for y in range(top, top + height):
                coordinate_claim_ids[(x, y)].add(claim_id)
                if len(coordinate_claim_ids[(x, y)]) == 2:
                    part_1 += 1

    overlapped_claims = set()
    for claim_ids in coordinate_claim_ids.values():
        if len(claim_ids) > 1:
            overlapped_claims.update(claim_ids)

    part_2 = (all_claim_ids - overlapped_claims).pop()

    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    solve()
