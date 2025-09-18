x, y, n = input().split(" ")
x = int(x)
y = int(y)
n = int(n)

output = list(range(1, n + 1))

for i in range(x, n + 1, x):
    output[i - 1] = "Fizz"

for j in range(y, n + 1, y):
    if output[j - 1] == "Fizz":
        output[j - 1] = "FizzBuzz"
    else:
        output[j - 1] = "Buzz"


print("\n".join(str(num) for num in output))