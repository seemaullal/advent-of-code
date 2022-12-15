class Packet:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

    @classmethod
    def _compare(cls, item1, item2):
        if isinstance(item1, int) and isinstance(item2, int):
            if item1 == item2:
                return 0
            return -1 if item1 < item2 else 1
        elif isinstance(item1, list) and isinstance(item2, list):
            i = 0
            while i < len(item1) and i < len(item2):
                result = cls.compare(item1[i], item2[i])
                if result != 0:
                    return result
                i += 1
            if i == len(item1) == len(item2):
                return 0
            return -1 if len(item1) < len(item2) else 1
        elif isinstance(item1, list) and isinstance(item2, int):
            return cls.compare(item1, [item2])
        else:
            return cls.compare([item1], item2)

    def __eq__(self, other):
        return self.compare(self.value, other.value) == 0

    def __lt__(self, other):
        return self.compare(self.value, other.value) == -1


DIVISOR_PACKETS = [Packet([[2]]), Packet([[6]])]

with open("inputs/13.txt") as file:
    packets = []
    for line in file.read().splitlines():
        if line:
            packets.append(Packet(eval(line)))


def part_1():
    result = 0
    pair_number = 1
    for index in range(0, len(packets) - 1, 2):
        if packets[index] < packets[index + 1]:
            result += pair_number
        pair_number += 1
    return result


def part_2():
    result = 1
    for packet_number, packet in enumerate(sorted([*packets, *DIVISOR_PACKETS]), 1):
        if packet in DIVISOR_PACKETS:
            result *= packet_number
    return result


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
