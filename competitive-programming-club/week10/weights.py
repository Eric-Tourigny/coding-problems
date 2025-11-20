n = int(input())
the_weights = list(sorted(int(input()) for _ in range(n)))
UPPER_LIMIT = 2000
elements = [False] * UPPER_LIMIT
elements[0] = True

for weight in the_weights:
    for i, element in enumerate(list(elements)):
        if element:
            if i + weight < UPPER_LIMIT:
                elements[i + weight] = True

for u in range(1000):
    if elements[u + 1000]:
        break
else:
    u = 10000

for l in range(1000):
    if elements[1000 - l]:
        break
else:
    l = 10000

if u <= l:
    print(1000 + u)
else:
    print(1000 - l)
