n = int(input())
strings = ["{}"]
for i in range(1, n + 1):
    strings.append("{" + ",".join(strings[j] for j in range(i)) + "}")
print(strings[n])