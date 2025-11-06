n, M = map(int, input().split())

items = []
for i in range(n):
    P, C = map(int, input().split())
    items.append((P, C))

def get_profit(time):
    return sum(P * time - C for P, C in items if P * time - C > 0)


def binary_search(left, right):
    if left == right:
        return left
    
    mid = (left + right) // 2
    value = get_profit(mid)
    if value < M:
        return binary_search(mid + 1, right)
    else:
        return binary_search(left, mid)


print(binary_search(0, 10**10))

