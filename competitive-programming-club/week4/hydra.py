while True:
    H, T = map(int, input().split())
    if H == 0 and T == 0:
        break

    N = T % 2
    bs = (T + 1) // 2
    N += bs
    H += bs
    N += (H % 2) * 3
    N += (H + 1) // 2
    print(N)