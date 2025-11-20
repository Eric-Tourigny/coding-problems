n, a, b, c = map(int, input().split())

a_s = a
b_s = b
c_s = c

for i in range(n - 1):
    new_a_s = a * (b_s + c_s)
    new_b_s = b * (a_s + c_s)
    new_c_s = c * (a_s + b_s)
    a_s = new_a_s
    b_s = new_b_s
    c_s = new_c_s

print((a_s + b_s + c_s) % (10 ** 9 + 7))