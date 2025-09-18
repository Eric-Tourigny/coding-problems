def get_divisors(x):
    for i in range(1, x):
        if x % i == 0:
            yield i

while(value := input()):
    value = int(value)
    total = sum(get_divisors(value))
    if total == value:
        print(f"{value} perfect")
    elif value - 2 <= total <= value + 2:
        print(f"{value} almost perfect")
    else:
        print(f"{value} not perfect")