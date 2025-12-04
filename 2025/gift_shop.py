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

def any_sequence(start, end, seq:list):
    pattern = r"^(\d+)\1+$"
    for number in range(start, end+1):
        if re.search(pattern,str(number)):
            seq.append(number)
    return seq
        

# Preparing The Data
with open("./002_live.txt") as file:
    data = file.read().split(',')
    
x = []
for r in data:
    range_start = int(r.split('-')[0])
    range_end = int(r.split('-')[1])
    double_sequence(range_start,range_end,x)

y = []
for r in data:
    range_start = int(r.split('-')[0])
    range_end= int(r.split('-')[1])
    any_sequence(range_start, range_end, y)
# double_sequence(11,22, x)
# double_sequence(998,1012,x)
print(sum(x))
print(sum(y))