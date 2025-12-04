"""
Code for Advent of Code
Year: 2025
Day: 03/12
"""

import re
import itertools

def Maximum_Joltage_1(filepath):
    MAXIMUM_JOLTAGE = 0
    with open(filepath) as file:
        data = file.read().strip().splitlines()
    for battery in data:
        jolts = []
        digits = [d for d in battery]
        # print(digits)
        combo = list(itertools.combinations(digits, 2))
        for c in combo:
            jolts.append("".join(c))
        MAXIMUM_JOLTAGE += int(max(jolts))
    return MAXIMUM_JOLTAGE

def Maximum_Joltage_2(filepath):
    output = 0
    with open(filepath) as file:
        data = file.read().strip().splitlines()
    for battery in data:
        jolts = []
        digits = [d for d in battery]
        combo = list(itertools.combinations(digits,12))
        for c in combo:
            jolts.append("".join(c))

        output += int(max(jolts))
    print(output)

Maximum_Joltage_2("./003_live.txt")