a, c = map(int, input().split())

cutoff = 10 ** 6
total = 1
values = list(range(2, cutoff))

for value in values:
    if value != -1:
        if a % value == 0 or c % value == 0:
            count = 0
            while a % value == 0:
                a /= value
                count += 1
            while c % value == 0:
                c /= value
                count += 1
            total *= count + 1

        number = value
        while number < cutoff:
            values[number - 2] = -1
            number += value

print(total)