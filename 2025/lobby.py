"""
Code for Advent of Code
Year: 2025
Day: 03/12
"""

import re
import itertools

MAXIMUM_JOLTAGE = 0

# Opening Data
with open("./003_test.txt") as file:
    data = file.read().strip().splitlines()

for battery in data:
    jolts = []
    digits = [d for d in battery]
    # print(digits)
    combo = list(itertools.combinations(digits, 2))
    for c in combo:
        jolts.append("".join(c))
    MAXIMUM_JOLTAGE += int(max(jolts))

print(MAXIMUM_JOLTAGE)


# Proof of Concept:
# b = ['8', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '9']
# n = [i for i in zip(b,b)]
# c = itertools.combinations(b,2)

# print(n)

# jolt = []

# for t in c:
#     jolt.append("".join(t))

# print(max(jolt))