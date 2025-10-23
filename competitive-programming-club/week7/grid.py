import math
from collections import deque

n, m = map(int, input().split())

grid = []
for i in range(n):
    row = []
    row_text= input()
    for char in row_text:
        row.append(int(char))
    grid.append(row)

path_lengths = [[math.inf] * m for i in range(n)]

jobs: deque[tuple[int, int, int]] = deque()
jobs.append((0, 0, 0))

def dfs(i, j, path_length):
    if 0 <= i < n and 0 <= j < m:
        if path_length < path_lengths[i][j]:
            value = grid[i][j]
            path_lengths[i][j] = path_length
            jobs.append((i + value, j, path_length + 1))
            jobs.append((i - value, j, path_length + 1))
            jobs.append((i, j + value, path_length + 1))
            jobs.append((i, j - value, path_length + 1))

try:
    while True:
        dfs(*jobs.popleft())
except:
    pass

final_value = path_lengths[n - 1][m - 1]
if final_value is math.inf:
    final_value = -1
print(final_value)