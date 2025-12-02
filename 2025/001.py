import re

# Test Data
with open("D:/GitHub/AdventOfCode/2025/001_test.txt") as file:
    data = file.read().strip().splitlines()

only_nums = []
dial = 50
zeroes = 0

for entry in data:
    pattern = entry.split()
    for item in pattern:
        alg = re.split(r'(L|R)', item)
        print(alg)