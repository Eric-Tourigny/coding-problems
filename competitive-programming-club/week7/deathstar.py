n = int(input())

values = []
for r in range(n):
    value = 0
    row = map(int, input().split())
    for number in row:
        value |= number
    values.append(value)

print(" ".join(str(value) for value in values))