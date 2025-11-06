import sys
sys.setrecursionlimit(10**8)

n = int(input())

items = [tuple(map(int, input().split())) for _ in range(n)]


def get_size(values, time):
    positions = [p + v * time for p, v in values]
    minimum = min(positions)
    maximum = max(positions)
    return maximum - minimum

def ternary_search(values, left, right):
    if (right - left) < 10 ** -8:
        return (right + left) / 2

    step = (right - left) / 3
    mid_left = left + step
    size1 = get_size(values, mid_left)
    mid_right = mid_left + step
    size2 = get_size(values, mid_right)

    if (size1 < size2):
        return ternary_search(values, left, mid_right)
    else:
        return ternary_search(values, mid_left, right)

time = ternary_search(items, 0, 10 ** 6)
print(get_size(items, time))