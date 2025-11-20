from functools import cache

@cache
def get_combinations(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return get_combinations(n - 3) + get_combinations(n - 2)  + get_combinations(n - 1)

print(get_combinations(int(input())))