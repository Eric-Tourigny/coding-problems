loop = 0
while((n := int(input())) != 0):
    loop += 1
    names = []
    for i in range(n):
        names.append(input())
    reordered = [None] * n 
    for i in range(n):
        if i % 2 == 0:
            reordered[i // 2] = names[i]
        else:
            reordered[n - (i + 1) // 2] = names[i]
    print(f"SET {loop}")
    for name in reordered:
        print(name)