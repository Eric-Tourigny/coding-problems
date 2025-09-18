thresholds = input().split(" ")
thresholds = [int(x) for x in thresholds]
grades = ["A", "B", "C", "D", "E"]
grade = int(input())

for letter, threshold in zip(grades, thresholds):
    if grade >= threshold:
        print(letter)
        break
else:
    print("F")
