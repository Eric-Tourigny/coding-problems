n = int(input())

entries = []

for i in range(int(n / 2) - 1):
    entries.append("2")

if n % 2 == 0:
    entries.append("2")
else:
    entries.append("3")

print(len(entries))
print(" ".join(entries))