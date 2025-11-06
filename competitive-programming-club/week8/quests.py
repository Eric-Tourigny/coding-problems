import bisect
import math

values = []

n = int(input())
for i in range(n):
    command, *array = input().split()
    if command == "add":
        E, G = map(int, array)
        index = bisect.bisect_right(values, (E, G))
        values.insert(index, (E, G))
    if command == "query":
        gold = 0
        energy = int(array[0])
        while True:
            index = bisect.bisect_right(values, (energy, math.inf))
            if index == 0:
                print(gold)
                break
            else:
                (E, G) = values.pop(index - 1)
                energy -= E
                gold += G
