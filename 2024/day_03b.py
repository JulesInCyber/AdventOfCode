import re

test_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()??mul(8,5))"

# enabled = re.findall("do\(\).*(?!don't\(\)).*mul\(\d+,\d+\).*", test_string)

split = re.split("(do\(\)|don't\(\))", test_string)

enabled = []
skip = False

for item in split:
    if skip:
        skip = False
        continue
    elif item == "don't()":
        skip = True
        continue
    enabled.append(item)

enabled = "".join(enabled)
statements = "".join(re.findall("mul\(\d+,\d+\)", enabled))
print(statements)
nums = re.findall("\d+", statements)
nums = [int(x) for x in nums]
print(nums)
prod = [a * b for a,b in zip(nums[1::2],nums[::2])]
prodsum = sum(prod)

print(prodsum)