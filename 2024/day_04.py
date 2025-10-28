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

def forward_col(grid: list[list[str]], pattern: str) -> int:
    count = 0
    max_rows = len(grid)
    max_cols = len(grid[0])
    pattern = list(pattern) # Each Letter as list-entry
    for row in range(max_rows):
        for col in range(max_cols):
            if grid[row][col] == 'X':
                if row + 1 < max_cols:
                    if grid[row+1][col] == 'M':
                        if row + 2 < max_cols:
                            if grid[row+2][col] == 'A':
                                if row + 3 < max_cols:
                                    if grid[row+3][col] == 'S':
                                        count += 1
    return count


fr = forward_row(data, "XMAS")
br = backward_row(data, "SAMX")
fc = forward_col(nested, "XMAS")
print(fc)
print(fr + br)