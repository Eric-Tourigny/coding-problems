n = int(input())

y_total = 0
y_streak = 0
y_best_streak = 0
y_best_lead = 0

n_total = 0
n_streak = 0
n_best_streak = 0
n_best_lead = 0

for i in range(n):
    if input() == "Yraglac":
        y_total += 1
        y_best_lead = max(y_best_lead, y_total - n_total)
        y_streak += 1
        n_streak = 0
        y_best_streak = max(y_best_streak, y_streak)
    else:
        n_total += 1
        n_best_lead = max(n_best_lead, n_total - y_total)
        n_streak += 1
        y_streak = 0
        n_best_streak = max(n_best_streak, n_streak)

resultA = "N"
resultB = "N"

if y_best_streak > n_best_streak:
    resultA = "Y"
elif y_best_streak == n_best_streak:
    resultA = "T"


if y_best_lead > n_best_lead:
    resultB = "Y"
elif y_best_lead == n_best_lead:
    resultB = "T"

if resultA == resultB:
    print("Agree")
else:
    print("Disagree")