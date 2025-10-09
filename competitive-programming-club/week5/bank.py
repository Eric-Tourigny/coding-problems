N, T = map(int, input().split())

positions = [None] * 500

class PriorityQueue:
    def __init__(self):
        self.list = []

    def push(self, elem):
        self.list.append(elem)
     
    def pop(self):
        value = max(self.list)
        self.list.remove(value)
        return value
    
queue = PriorityQueue()
for i in range(N):
    money, time = map(int, input().split())
    queue.push((money, time))

def add(a_money, a_time):
    global positions
    while a_time >= 0:
        if positions[a_time] is None:
            positions[a_time] = a_money
            break
        a_time -= 1

for i in range(N):
    try:
        add(*queue.pop())
    except:
        pass

positions = [value if value is not None else 0 for value in positions]

print(sum(positions))