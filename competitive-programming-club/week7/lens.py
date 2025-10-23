from math import atan, tan
d, x, y, h = map(int, input().split())
theta_0 = atan((y - h / 2) / x)
theta_1 = atan(y / x) - theta_0
theta_2 = atan((y + h / 2) / x) - theta_1 - theta_0
a = d * (tan(theta_1) + tan(theta_2))
print(a)