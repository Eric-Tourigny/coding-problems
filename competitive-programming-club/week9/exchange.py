while (n := int(input())) != 0:
    best_canadian = 100000 # cents
    best_american = 0
    for i in range(n):
        rate = float(input())
        best_american = max(best_american, int(best_canadian / rate * 0.97))
        best_canadian = max(best_canadian, int(best_american * rate * 0.97))
    print(f"{best_canadian / 100 :.2f}")
