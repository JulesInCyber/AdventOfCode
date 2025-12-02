import re

# Test Data
with open("D:/GitHub/AdventOfCode/2025/001_test.txt") as file:
    data = file.read().strip().splitlines()

def get_algorithm(data):
    algorithm = []
    for entry in data:
        pattern = entry.split()
        for item in pattern:
            alg = re.split(r'(L|R)', item)
            filtered = [i for i in alg if i != ""]
            algorithm.append(filtered)
    return algorithm

def turn_dial(dial_start, instructions):
    zeroes = 0
    for i in instructions:
        # print(f"Dial at: {dial_start}")
        if dial_start == 0:
            zeroes += 1
        if i[0] == "L":
            result = dial_start - int(i[1])
            dial_start = result % 100
        elif i[0] =="R":
            result = dial_start + int(i[1])
            dial_start = result % 100
    code = f"The Code is: {zeroes}"
    return code  

def method_0x434C49434B(dial_start, instructions):
    '''
    - Number of times dial hits 0 --> Done
    - Number of times dial crosses 0
    '''
    clicks = 0
    for i in instructions:
        old_dial = dial_start
        #print(f"Older: {dial_start}")
        if i[0] == "L":
            result = dial_start - int(i[1])
            # print(f"L Result is: {result}")
            dial_start = result % 100
        elif i[0] =="R":
            result = dial_start + int(i[1])
            # print(f"R Result is: {result}")
            dial_start = result % 100
        if dial_start == 0:
            clicks += 1

    code = f"The Code is: {clicks}"
    return code


instructions = get_algorithm(data)
code = method_0x434C49434B(50, instructions)

print(code)

