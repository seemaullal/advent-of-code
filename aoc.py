#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

import requests
import sys
import os
import subprocess
from datetime import datetime

if len(sys.argv) < 2:
    raise Exception("Pass in a day number so we know what day to download.")

day_number = sys.argv[1]
year = datetime.now().year

input_contents = requests.get(
    f"https://adventofcode.com/{year}/day/{day_number}/input",
    cookies={"session": os.environ.get("AOC_SESSION")},
).text

filename = (
    f"/Users/seema/dev/advent-of-code/{year}/{day_number:0>{2}}/{day_number:0>{2}}.py"
)
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as f:
    pass

with open(
    f"/Users/seema/dev/advent-of-code/{year}/inputs/{day_number}.txt", "w"
) as file:
    file.write(input_contents)

year = datetime.now().year
subprocess.run(["open", f"https://adventofcode.com/{year}/day/{day_number}"])
subprocess.run(["code", "/Users/seema/dev/advent-of-code"])
