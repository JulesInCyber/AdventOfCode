import re

def double_sequence(start, end, seq:list=[]):
    '''
    Data contains ranges separated by commas (',')
    Start and end of range is separated by dash ('-')

    Function finds all sequences of digits that are repeated twice
    within a range:
    11-22 --> 11, 22
    95-115 --> 99
    998-1015 --> 1010
    '''
    pattern = r"^(\d+)\1$"
    for number in range(start, end+1):
        if re.search(pattern, str(number)):
            seq.append(number)
    return seq
# Preparing The Data
with open("./002_test.txt") as file:
    data = file.read().split(',')

# sum = 0
# # Iteration through ranges
# for numbers in data:
#     range_start = int(numbers.split('-')[0])
#     range_end = int(numbers.split('-')[1])+1
#     pattern = r"^(\d+)\1+$" # delete the last '+' for exactly 2
#     for num in range(range_start,range_end):
#         if re.search(pattern, str(num)):
#             sum += num

# print(sum)

x = []
for r in data:
    range_start = int(r.split('-')[0])
    range_end = int(r.split('-')[1])
    double_sequence(range_start,range_end,x)

# double_sequence(11,22, x)
# double_sequence(998,1012,x)
print(sum(x))