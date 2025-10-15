r, f = map(int, input().split())

quarter_rotations = f / r * 2

if int(quarter_rotations % 4) in (0, 3):
    print("up")
else:
    print("down")