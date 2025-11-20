import bisect

n = int(input())
the_weights = list(sorted(int(input()) for _ in range(n)))
size = len(the_weights)

def abs_min(a, b):
    if abs(a) == abs(b):
        if a > 0:
            return a
        else:
            return b
    elif abs(a) < abs(b):
        return a
    else:
        return b

def recursive_solve(target: int, i: int):
    value = the_weights[i]
    new_target = target - value
    if new_target < 0:
        return -new_target

    next_larger = bisect.bisect_right(the_weights, new_target, 0, i)
        
    if next_larger < i:
        best_result  = the_weights[next_larger] - new_target
    else:
        best_result = 10000

    if next_larger == 0:
        best_result = abs_min(best_result, value - target)
    else:
        best_result = abs_min(best_result, recursive_solve(target - value, next_larger - 1))

        best_result = abs_min(best_result, recursive_solve(target, i - 1))
        
    return best_result

print(1000 + recursive_solve(1000, size - 1))
