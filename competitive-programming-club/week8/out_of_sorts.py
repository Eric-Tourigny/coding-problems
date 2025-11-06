n, m, a, c, x0 = map(int, input().split())

current_value = x0
values = []

for i in range(n):
    new_value = (a * current_value + c) % m
    values.append(new_value)
    current_value = new_value

def binary_sweep(left, right, minimum, maximum):
    if left >= 0 and right >= 0 and left < m and right < m:
        total = 0
        mid = (left + right) // 2
        value =  values[mid]
        if minimum < value < maximum:
            total = 1

        if left >= right:
            return total
        
        total += binary_sweep(left, mid - 1, minimum, min(maximum, value))
        total += binary_sweep(mid + 1, right, max(minimum, value), maximum)
        return total
    else:
        return 0

print(binary_sweep(0, len(values) - 1, -1, m))