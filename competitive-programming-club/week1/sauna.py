n = int(input())
lower = []
upper = []
for line in range(n):
    x, y = input().split()
    lower.append(int(x))
    upper.append(int(y))

minimum = max(lower)
maximum = min(upper)

if (minimum < maximum):
    print(f"{maximum - minimum + 1} {minimum}")
else:
    print("bad news")