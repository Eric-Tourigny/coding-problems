import bisect

class RainData:
    def __init__(self, date, amount, largest_since, last_hole):
        self.date = date
        self.amount = amount
        self.largest_since: None | RainData = largest_since
        self.last_hole = last_hole
    
    def __repr__(self):
        return f"{self.date}: {self.amount}"

while True:
    n = int(input())
    if n == 0:
        break

    rains: list[RainData] = []
    largest_rains: list[RainData] = []
    length = 0
    last_year = None
    for _ in range(n):
        y, r = map(int, input().split())

        if last_year is None or y - last_year != 1:
            last_hole = y - 1

        new_data = RainData(y, r, None, last_hole)
        rains.append(new_data)

        index = bisect.bisect_right(largest_rains, -new_data.amount, 0, length, key= lambda x: -x.amount)
        if index != 0:
            new_data.largest_since = largest_rains[index - 1]
            
            while index != 0:
                if largest_rains[index - 1].amount == r:
                    index -= 1
                else:
                    break

        if index < len(largest_rains):
            largest_rains[index] = new_data
        else:
            largest_rains.append(new_data)
        
        length = index + 1
        last_year = y

    largest_rains = largest_rains[:length]

    m = int(input())
    for _ in range(m):
        y1, y2 = map(int, input().split())

        index1 = bisect.bisect_right(rains, y1, key=lambda x: x.date) - 1
        index2 = bisect.bisect_right(rains, y2, key=lambda x: x.date) - 1

        if index1 < 0:
            if index2 < 0:
                print("maybe")
            else:
                year2 = rains[index2]
                if year2.largest_since == None or year2.date != y2:
                    print("maybe")
                else:
                    print("false")
        else:
            year1 = rains[index1]
            year2 = rains[index2]

            if year2.date == y2:
                if year2.largest_since is year1:
                    if year2.last_hole is None or year2.last_hole < y1:
                        print("true")
                    else:
                        print("maybe")
                else:
                    if year1.date == y1:
                        print("false")
                    else:
                        if year2.largest_since is not None and year2.largest_since.date > y1:
                            print("false")
                        else:
                            print("maybe")
            else:
                if year2 is year1:
                    print("maybe")
                elif y1 == year1.date:
                    current_year = year2
                    last_value = None
                    while current_year is not None and current_year.date > y1:
                        last_value = current_year.amount
                        current_year = current_year.largest_since
                        
                    if current_year is year1:
                        if year1.amount == last_value:
                            print("false")
                        else:
                            print("maybe")
                    else:
                        print("false")
                else:
                    print("maybe")  

    print()
    input()
