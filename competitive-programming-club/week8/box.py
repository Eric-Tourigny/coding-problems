import math
n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    h = (x + y - math.sqrt(x * x - x * y + y * y)) / 6

    print(h * (x - 2 * h) * (y - 2 * h))