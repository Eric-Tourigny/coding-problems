D, U = map(int, input().split())

prime_factors = []
num_occurences = []

numbers_made = [True] * (10**6 + 2)

def factorize(number):
    for i in range(2, len(numbers_made)):
        if numbers_made[i]:
            occurences = 0
            while number % i == 0:
                number /= i
                occurences += 1
                if number == 1:
                    break
            if occurences > 0:
                prime_factors.append(i)
                num_occurences.append(occurences)
                for j in range(i, len(numbers_made), i):
                    numbers_made[j] = False


factorize(D)

values: dict[int, list[int]] = {}
done: set[int] = set()

values[1] = [0] * len(prime_factors)


max_greater_than = D

while values:
    current_total, composition = values.popitem()

    if U <= current_total < max_greater_than:
        max_greater_than = current_total

    for ip, prime in enumerate(prime_factors):
        if composition[ip] < num_occurences[ip]:
            new_total = current_total * prime
            if new_total not in values and new_total not in done:
                new_composition = composition.copy()
                new_composition[ip] = new_composition[ip] + 1
                values[new_total] = new_composition
                done.add(new_total)
    
print(max_greater_than)

