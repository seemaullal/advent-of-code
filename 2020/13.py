import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/13.txt"

with open(input_file) as file:
    earliest_bus_time = int(file.readline())
    bus_ids = [bus_id if bus_id == 'x' else int(bus_id) for bus_id in file.readline().split(",")]

def gcd(a,b):
    if a==0 or b==0:
        return a+b
    if a>b:
        return gcd(a%b,b)
    return gcd(a,b%a)


def part_1():
    current_time = earliest_bus_time
    while True:
        for bus_id in bus_ids:
            if bus_id != 'x' and current_time % bus_id == 0:
                return (current_time - earliest_bus_time) * bus_id
        current_time += 1


def part_2():
    busses_with_position = [(index, bus_id) for index, bus_id in enumerate(bus_ids) if bus_id != 'x']
    time = 0
    step_size = 1
    found_bus_ids = set()
    while len(found_bus_ids) != len(busses_with_position):
        time += step_size
        for index, bus in busses_with_position:
            if (time + index) % bus != 0:
                break
            elif bus not in found_bus_ids:
                found_bus_ids.add(bus)
                step_size = (bus * step_size) // gcd(bus, step_size)
    return time


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
