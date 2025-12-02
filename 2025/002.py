import re
import numpy as np

# Function
def invalid_id(start, end):
    id = []
    # Sequence of digits repeated twice
    search_pattern = r"^(\d+)\1"
    for number in range(start, end+1):
        if  re.search(search_pattern, str(number)):
            id.append(number)
    return id

# Preparing The Data
with open("002_test.txt") as file:
    data = file.read().split(',')

sum = 0
# Iteration through ranges
for numbers in data:
    range_start = int(numbers.split('-')[0])
    range_end = int(numbers.split('-')[1])+1
    pattern = r"^(\d+)\1$"
    for num in range(range_start,range_end):
        if re.search(pattern, str(num)):
            sum += num

# print(sum)

invalid = invalid_id(11,22)
# sum = [np.sum(x) for x in invalid]
x = np.sum(invalid)
print(x)