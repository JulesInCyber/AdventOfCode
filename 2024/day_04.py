import re

# Importing input
with open ("test.txt") as file:
    data = file.read().splitlines()

nested = [list(i) for i in data]
# Forward Search Rows
def row_search(grid: list[str], pattern: str) -> int:
    count = 0
    for row in grid:
        matches = re.findall(pattern, row)
        if matches:
            count += 1
    return count

def col_search(grid: list[list[str]], pattern: str) -> int:
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

def dia_search(grid, pattern):
    count = 0
    max_rows = len(grid)
    max_cols = len(grid[0])
    pattern_length = len(pattern)

    for row in range(max_rows - pattern_length + 1):
        for col in range(max_cols - pattern_length + 1):
            word = ''.join(grid[row+i][col+i] for i in range(pattern_length))
            if word == pattern:
                count += 1
    return count
pat = "XMAS"


row_match = row_search(data, pat) + row_search(data, pat[::-1])
col_match = col_search(nested, pat) + col_search(nested, pat[::-1])
dia_match = dia_search(nested, pat) + dia_search(nested, pat[::-1])

total = row_match + col_match + dia_match

print(total)