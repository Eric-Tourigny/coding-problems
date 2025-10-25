import bisect

n = int(input())

class RainData:
    def __init__(self, date, amount, largest_since):
        self.date = date
        self.amount = amount
        self.largest_since = largest_since
    
    def __lt__(self, other: "RainData"):
        return self.amount > other.amount

    def __repr__(self):
        return f"{self.date}: {self.amount}"


rains: dict[int, RainData] = {}
largest_rains = []
for _ in range(n):
    y, r = map(int, input().split())
    new_data = RainData(y, r, None)
    rains[y] = new_data

    index = bisect.bisect_right(largest_rains, new_data)
    if index != 0:
        new_data.largest_since = largest_rains[index - 1]

    largest_rains = largest_rains[:index]
    largest_rains.append(new_data)

m = int(input())
for _ in range(m):
    y1, y2 = map(int, input().split())
    early_year = rains[y1]
    late_year = rains[y2]
    if late_year.largest_since is early_year:
        print("true")
    else:
        print("false")
