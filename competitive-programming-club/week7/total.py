n = int(input())

numbers = []
for i in range(n):
    numbers.append(int(input()))

left = 0
right = sum(numbers)
max_product = 0

for value in numbers:
    left += value ** 2
    right -= value
    max_product = max(max_product, left * right)

print(max_product)