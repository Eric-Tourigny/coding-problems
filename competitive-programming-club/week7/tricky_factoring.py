a, c = map(int, input().split())

a_cur = a
c_cur = c

cutoff = 10 ** 6
a_prime_factors = {}
c_prime_factors = {}
values = list(range(cutoff))

iterator = iter(values)
next(iterator)  # discard 2
next(iterator)  # discard 1
for value in iterator:
    if value != -1:
        if a_cur % value == 0:
            count = 0
            while a_cur % value == 0:
                a_cur /= value
                count += 1
            a_prime_factors[value] = count
            if a_cur == 1 and c_cur == 1:
                break
        if c_cur % value == 0:
            count = 0
            while c_cur % value == 0:
                c_cur /= value
                count += 1
            c_prime_factors[value] = count
            if a_cur == 1 and c_cur == 1:
                break
        number = value
        while number < cutoff:
            values[number] = -1
            number += value

z_prime_factors = {}
for factor, count in a_prime_factors.items():
    z_prime_factors[factor] = count
for factor, count in c_prime_factors.items():
    if factor in z_prime_factors:
        z_prime_factors[factor] += count
    else:
        z_prime_factors[factor] = count

total = 1
for factor, count in z_prime_factors.items():
    total *= count + 1
print(total) 
