w, h = map(int, input().split())
n, m = map(int, input().split())

import math

asteroids = list()
for i in range(n):
    asteroids.append(tuple(map(int, input().split())))

positions = list()
for j in range(m):
    positions.append(tuple(map(int, input().split())))

hit = False
for xr, yr in positions:
    for xa, ya, ra in asteroids:
        if   xr <= xa <= xr + w and yr - ra <= ya <= yr + ra + h:
            hit = True
        elif yr <= ya <= yr + h and xr - ra <= xa <= xr + ra + w:
            hit = True
        else:
            d = math.inf

            if   xa < xr and ya < yr:
                d = math.sqrt((xr - xa) ** 2 + (yr - ya) ** 2)
            elif xa > xr + w and ya < yr:
                d = math.sqrt((xr + w - xa) ** 2 + (yr - ya) ** 2)
            elif xa < xr and ya > yr + h:
                d = math.sqrt((xr - xa) ** 2 + (yr + h - ya) ** 2)
            elif xa > xr + w and ya > yr + h:
                d = math.sqrt((xr + w - xa) ** 2 + (yr + h - ya) ** 2)
            
            if d <= ra:
                hit = True
        
    if hit:
        print("DOOMSLUG STOP!")
    else:
        print("DOOMSLUG GO!")

    hit = False
