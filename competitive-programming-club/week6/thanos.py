n = int(input())

for i in range(n):
    P, R, F = map(int, input().split())
    if P > F:
        print(0)
        continue

    for i in range(1, 10**9):
        P *= R
        if P > F:
            print(i)
            break