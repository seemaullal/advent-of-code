import sys
import time
from collections import defaultdict

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/24.txt"
with open(input_file) as file:
    lines = [line.strip().split()[-1] for line in file]

class ModelNumbers:
  def __init__(self, rules):
    self._params = list(zip(rules[5::18], rules[4::18], rules[15::18]))
    self._params = [tuple(int(i) for i in params) for params in self._params]

  def find_valid_model_nums(self):
    valid_tails = self._valid_tails(0)
    return {int(num) for num in valid_tails[0]}

  def _valid_tails(self, level):
    if level == 14:
      return {0: {""}}

    valid_tails = defaultdict(set)
    sub, div, offset = self._params[level]
    for z_out, tails in self._valid_tails(level + 1).items():
      for z_in in [z_out * div + i for i in range(div)]:
        for w in range(1, 10):
          if z_in % 26 + sub == w:
            valid_tails[z_in].update({f"{w}{tail}" for tail in tails})
      for w in range(1, 10):
        z_pre = z_out - w - offset
        # invalid
        if z_pre < 0 or z_pre % 26 != 0:
          continue
        z_pre = z_pre // 26
        for z_in in [z_pre * div + i for i in range(div)]:
          if z_in % 26 + sub != w:
            valid_tails[z_in].update({f"{w}{tail}" for tail in tails})
    return valid_tails

  def run(self, inp):
    z = 0
    for level, w in enumerate(str(inp)):
      z = self._op(z, w, level)
    return z

  def _op(self, z, w, level):
    sub, div, offset = self._params[level]
    w = int(w)
    x = z % 26 + sub == w
    z = z // div
    if not x:
      z = 26 * z + w + offset
    return z


def part_1():
  return max(ModelNumbers(lines).find_valid_model_nums())


def part_2():
  return min(ModelNumbers(lines).find_valid_model_nums())


start = time.perf_counter()
print(f"Part 1: {part_1()}")
stop = time.perf_counter()
print(f"Finished Part 1 in {stop - start:0.4f} seconds")
start = time.perf_counter()
print(f"Part 2: {part_2()}")
stop = time.perf_counter()
print(f"Finished Part 2 in {stop - start:0.4f} seconds")