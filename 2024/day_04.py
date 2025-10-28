import re

with open ("test.txt") as file:
    data = file.read().splitlines()

nested = [list(i) for i in data]

# Grid Dimension
max_rows = len(nested)
max_cols = len(nested[0])

# Forward Search Rows
def forward_row(grid: list[str], pattern: str) -> int:
    count = 0
    for row in grid:
        matches = re.findall(pattern, row)
        if matches:
            count += 1
    return count

# Backwards Search Rows
def backward_row(grid: list[str], pattern: str) -> int:
    count = 0
    for row in grid:
        matches = re.findall(pattern[::-1], row)
        if matches:
            count  += 1
    return count

def forward_col(grid: list[list[str]], pattern: str) -> int:
    count = 0
    max_rows = len(grid)
    max_cols = len(grid[0])
    pattern_length = len(pattern)
    for row in range(max_rows - pattern_length + 1):
        for col in range(max_cols):
            word = ''.join(grid[row+i][col] for i in range(pattern_length))
            if word == pattern:
                count += 1
    return count

def backward_col(grid: list[list[str]], pattern: str) -> int:
    count = 0
    max_rows = len(grid)
    max_cols = len(grid[0])
    pattern_length = len(pattern)
    for row in range(max_rows - pattern_length + 1):
        for col in range(max_cols):
            word = ''.join(grid[row+i][col] for i in range(pattern_length))
            if word == pattern[::-1]:
                count += 1
    return count


pat = "XMAS"

fr = forward_row(data, pat)
br = backward_row(data, pat)
fc = forward_col(nested, pat)
bc = backward_col(nested, pat)
print(fc)
print(fr + br)