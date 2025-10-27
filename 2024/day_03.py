import re

def memory(message: str):
    # Searching for the correct pattern
    statements = "".join(re.findall("mul\(\d+,\d+\)", message))
    
    # Extrating the numbers to perform math
    nums = re.findall("\d+", statements)
    nums = [int(x) for x in nums]

    # Calculating the Products and adding them up
    prod = [a * b for a,b in zip(nums[1::2],nums[::2])]
    prodsum = sum(prod)
    return prodsum

test_string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

with open("input03.txt") as f:
    data = f.read()

result = memory(data)
print(result)