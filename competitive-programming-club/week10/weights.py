import functools

n = int(input())
the_weights = tuple(int(input()) for _ in range(n))


def return_better(target, value1, value2):
    if abs(target - value1) == abs(target - value2):
        if target - value1 < 0:
            return value1
        else:
            return value2
    elif abs(target - value1) < abs(target - value2):
        return value1
    else:
        return value2

@functools.cache
def closest(target: int, weights: tuple[int]):
    print(weights)
    if len(weights) == 0:
        print(target)
        return target
    else:
        best_diff = float("inf")
        for i, weight in enumerate(weights):
            best_diff = return_better(target, closest(target - weight, tuple(weight for j, weight in enumerate(weights) if j != i)), best_diff)
            best_diff = return_better(target, closest(target, tuple(weight for j, weight in enumerate(weights) if j != i)), best_diff)
        return best_diff


print(closest(1000, the_weights))