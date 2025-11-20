n, m = map(int, input().split())

total = 0
if m > n:
    total += m - n
    m = n

def generate_combinations(num):
    current = 1
    for r in range(num):
        yield r, current
        current = current * (num - r) / (r + 1)
    yield num, current

number = 0
for r, comb in generate_combinations(n):
    if r >= m:
        break
    number += comb * (m - r)

total += number / 2**n
if int(total) == total:
    print(int(total))
else:
    print(total)
