a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

operators = ["+", "-", "*", "/"]

def eval_operators(x, y):
    for operator in operators:
        t = eval(f"{x} {operator} {y}")
        if t == int(t):
            yield int(t)

min_value = float("inf")
for t in eval_operators(a, b):
    for value in eval_operators(t, c):
        if value >= 0:
            min_value = min(min_value, int(value))

print(min_value)
