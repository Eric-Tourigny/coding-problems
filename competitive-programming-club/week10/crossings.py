crossings = input()

best_north = 0
best_south = 1

for letter in crossings:
    match letter:
        case "S":
            best_north = min(best_north, best_south + 1)
            best_south = min(best_south + 1, best_north + 1)
        case "N":
            best_north = min(best_north + 1, best_south + 1)
            best_south = min(best_north + 1, best_south)    
        case "B":
            best_north = min(best_north + 1, best_south + 2)
            best_south = min(best_north + 2, best_south + 1)

print(best_north)