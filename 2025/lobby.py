import re

# Opening Data
with open("./003_test.txt") as file:
    data = file.read().strip().splitlines()

for battery in data:
    digits = [d for d in battery]
    highest = max(digits)
    print(highest)
    highest_index = digits.index(highest)
    sub_list = digits[highest_index+1:-1]
    print(sub_list)
