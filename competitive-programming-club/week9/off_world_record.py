n, c, p = map(int, input().split())

records = 0
for i in range(n):
    value = int(input())
    if value > c + p:
        p = c
        c = value
        records += 1
print(records)