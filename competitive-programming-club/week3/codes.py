k, n = input().split()
k = int(k)
n = int(n)

def is_present_in_order(super, sub):
    for c in super:
        if c == sub[0]:
            if len(sub) == 1:
                return True
            sub = sub[1:]
    return False

elongated_codes = []
for i in range(n):
    elongated_codes.append(input())

chars = list(str(i) for i in range(10))
current_possible = chars.copy()
next_possible = []

for i in range(k - 1):
    for string in current_possible:
        for char in chars:
            if all(is_present_in_order(code, string + char) for code in elongated_codes):
                next_possible.append(string + char)
    current_possible = next_possible.copy()
    next_possible = []

current_possible.sort()
print(len(current_possible))
for output in current_possible:
    print(output)