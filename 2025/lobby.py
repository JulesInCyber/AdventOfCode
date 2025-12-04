"""
Code for Advent of Code
Year: 2025
Day: 03/12
"""

import re
import itertools
MAXIMUM_JOLTAGE = 0

# Opening Data
with open("./003_live.txt") as file:
    data = file.read().strip().splitlines()

# print(data)
for battery in data:
    jolts = []
    digits = [d for d in battery]
    # print(digits)
    combo = list(itertools.combinations(digits, 2))
    for c in combo:
        jolts.append("".join(c))
    MAXIMUM_JOLTAGE += int(max(jolts))

print(MAXIMUM_JOLTAGE)

# Maximum_Joltage(["987654321111111"])
