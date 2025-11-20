from collections import deque

m, n, s0 = map(int, input().split())
pairs = [tuple(map(int, input().split())) for i in range(n)]

best_results: list[int | None] = [None] * m
best_results[s0] = 0
locations: deque[int] = deque()
locations.append(s0)

try:
    while True:
        s = locations.popleft()
        moves = best_results[s]
        for ai, bi in pairs:
            s_next = (s * ai + bi) % m
            if best_results[s_next] is None:
                best_results[s_next] = moves + 1
                locations.append(s_next)
except IndexError:
    if best_results[0] is None:
        print(-1)
    else:
        print(best_results[0])
