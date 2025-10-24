'''
https://adventofcode.com/2024/day/1
'''
import random

# Generate two random lists that we want to compare
# l1 = [random.randint(0,9) for i in range(6)]
# l2 = [random.randint(0,9) for i in range(6)]

# Using input Lists
with open("input01.txt") as f:
    data = f.read().strip().splitlines()

l1 = []
l2 = []

for line in data:
    a, b = map(int, line.split())
    l1.append(a)
    l2.append(b)

# Sort the lists
l1.sort()
l2.sort()

i = 0
sum = 0

for entry in l1:
    dist = abs(l1[i] - l2[i])
    sum += dist
    i += 1
print(sum)