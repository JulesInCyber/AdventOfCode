import re

# Preparing The Data
with open("002_test.txt") as file:
    data = file.read().split(',')

results = []
# Iteration through ranges
for numbers in data:
    range_start = int(numbers.split('-')[0])
    range_end = int(numbers.split('-')[1])+1
    for i in range(range_start,range_end):
        pass

def find_pattern(start, end):
    pattern = r"(.+?)\1"
    results = []
    for num in range(start, end +1):
        if re.search(pattern, str(num)):
            results.append(num)
    return results

r = find_pattern(11,1111)
print(r)