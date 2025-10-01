m = int(input())
lines = []
for i in range(m):
    for j, c in enumerate(map(int, input().split())):
        if c != -1:
            lines.append(f"{i + 1} {j + 1} {c}")

print(len(lines))
for line in lines:
    print(line)
