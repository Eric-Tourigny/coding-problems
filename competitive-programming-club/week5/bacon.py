while True:
    n = int(input())
    if n == 0:
        break

    mapping = {}

    for i in range(n):
        name, *items = input().split()
        for item in items:
            if item not in mapping:
                mapping[item] = []

            mapping[item].append(name)
        
    for item, names in sorted(mapping.items()):
        print(item, end=" ")
        for name in sorted(names):
            print(name, end=" ")
        print()
    print()