ds, ys = input().split()
ds = int(ds)
ys = int(ys)
dm, ym = input().split()
dm = int(dm)
ym = int(ym)

moon_date = -dm
moon_dates = []
while moon_date < 5000:
    moon_date += ym
    moon_dates.append(moon_date)

sun_date = -ds
sun_dates = []
while sun_date < 5000:
    sun_date += ys
    sun_dates.append(sun_date)

for date in sun_dates:
    if date in moon_dates:
        print(date)
        break
