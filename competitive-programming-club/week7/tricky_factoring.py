a, c = map(int, input().split())

a_cur = a
c_cur = c

cutoff = 10 ** 6
a_prime_counts = []
a_prime_factors = []
c_prime_counts = []
c_prime_factors = []
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
            a_prime_factors.append(value)
            a_prime_counts.append(count)
            if a_cur == 1 and c_cur == 1:
                break
        if c_cur % value == 0:
            count = 0
            while c_cur % value == 0:
                c_cur /= value
                count += 1
            c_prime_factors.append(value)
            c_prime_counts.append(count)
            if a_cur == 1 and c_cur == 1:
                break
        number = value
        while number < cutoff:
            values[number] = -1
            number += value

def generate_factors(prime_factors, prime_counts, number):
    cutoff = int(number ** 0.5)

    factors = [1]
    corresponding_factors = [number]
    for pf, count in zip(prime_factors, prime_counts):
        size = len(factors)

        multiplier = pf
        for i in range(count):
            for j in range(size):
                value = factors[j] * multiplier
                if value <= cutoff:
                    factors.append(value)
                    corresponding_factors.append(number / value)
            multiplier *= pf
    return factors, corresponding_factors

a_factors, a_corresponding_factors = generate_factors(a_prime_factors, a_prime_counts, a)
c_factors, c_corresponding_factors = generate_factors(c_prime_factors, c_prime_counts, c)


#a_factors = []
#a_corresponding = []
#for f in range(1, int(math.sqrt(a)) + 1):
#    if a % f == 0:
#        a_factors.append(f)
#        a_corresponding.append(a // f)
#
#c_factors = []
#c_corresponding = []
#for f in range(1, int(math.sqrt(c)) + 1):
#    if c % f == 0:
#        c_factors.append(f)
#        c_corresponding.append(c // f)

b_values = set()
for a1, a2 in zip(a_factors, a_corresponding_factors):
    for c1 in c_factors:
        c2 = c / c1
        b_values.add(a1 * c1 + a2 * c2)
        b_values.add(a1 * c2 + a2 * c1)

print(len(b_values) * 2)