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
        matches = re.findall(pattern, row)
        if matches:
            count  += 1
    return count

def forward_col(grid: list[list[str]]):
    pass

fr = forward_row(data, "XMAS")
br = backward_row(data, "SAMX")
print(fr + br)