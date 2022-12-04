import requests
import sys
import os

if len(sys.argv) < 2:
    raise Exception("Pass in a day number so we know what day to download.")

day_number = sys.argv[1]

input_contents = requests.get(
    f"https://adventofcode.com/2020/day/{day_number}/input",
    cookies={"session": os.environ.get("AOC_SESSION")},
).text

with open(f"inputs/{day_number}.txt", "w") as file:
    file.write(input_contents)
