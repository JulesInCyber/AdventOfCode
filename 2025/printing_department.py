"""
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

...
.@.
...

"""
import re

pattern = r"@"


# Function to count neighbors
def get_neighbors(grid,row,col):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1,-1),(-1,0),(-1,1),
                  (0,-1),(0,1),
                  (1,-1),(1,0),(1,1)]
    neighbors = []

    for dx, dy in directions:
        nr, nc = row + dx, col + dy
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append(grid[nr][nc])
    return neighbors

# Opening the data
with open("./004_test.txt") as file:
    data = file.read().strip().split()

data = [[char for char in s] for s in data]

# Counting Rolls that are accessible by forklifts
accessable = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "@":
            neighbors = get_neighbors(data, i, j)
            rolls = neighbors.count("@")
            if rolls < 4:
                accessable += 1


print(accessable)