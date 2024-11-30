import requests
import sys
import os
import subprocess
from datetime import datetime
from pathlib import Path

aoc_session = os.environ.get("AOC_SESSION")
if not aoc_session:
    sys.stderr.write(
        """You must export a value for AOC_SESSION in your environment for
this script to work. See https://github.com/seemaullal/advent-of-code
for further instructions."""
    )
    exit(1)

if len(sys.argv) < 2:
    raise Exception("Pass in a day number so we know what day to download.")

day_number = sys.argv[1].zfill(2)
if len(sys.argv) > 2:
    year = sys.argv[2]
else:
    year = datetime.now().year

sys.stdout.write(f"Downloading day {day_number} for {year}\n")

day_directory = f"{Path.cwd()}/{year}/{day_number}"

Path(f"{day_directory}/input").mkdir(exist_ok=True, parents=True)

input_contents = requests.get(
    f"https://adventofcode.com/{year}/day/{day_number}/input",
    cookies={"session": os.environ.get("AOC_SESSION")},
).text

with open(f"{day_directory}/input/{day_number}.txt", "w") as file:
    file.write(input_contents)

with open(f"{day_directory}/{day_number}.py", "w"):
    pass

subprocess.run(["open", f"https://adventofcode.com/{year}/day/{day_number}"])
subprocess.run(["code", Path.cwd()])
