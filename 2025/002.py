import re

# Preparing The Data
with open("./002_live.txt") as file:
    data = file.read().split(',')

sum = 0
# Iteration through ranges
for numbers in data:
    range_start = int(numbers.split('-')[0])
    range_end = int(numbers.split('-')[1])+1
    pattern = r"^(\d+)\1+$" # delete the last '+' for exactly 2
    for num in range(range_start,range_end):
        if re.search(pattern, str(num)):
            sum += num

print(sum)

# r = find_pattern(998,1012)
# print(r)