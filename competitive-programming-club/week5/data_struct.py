class Stack:
    def __init__(self):
        self.list = []
        self.works = True
        self.name = "stack"

    def push(self, elem):
        self.list.append(elem)
     
    def pop(self):
        return self.list.pop()

class Queue:
    def __init__(self):
        self.list = []
        self.works = True
        self.name = "queue"

    def push(self, elem):
        self.list.append(elem)
     
    def pop(self):
        return self.list.pop(0)

class PriorityQueue:
    def __init__(self):
        self.list = []
        self.works = True
        self.name = "priority queue"

    def push(self, elem):
        self.list.append(elem)
     
    def pop(self):
        value = max(self.list)
        self.list.remove(value)
        return value

def main(n):
    queues = [Stack(), Queue(), PriorityQueue()]
    for _ in range(n):
        op, element = map(int, input().split())
        for queue in queues:
            if queue.works:
                if op == 1:
                    queue.push(element)
                if op == 2:
                    try:
                        if queue.pop() != element:
                            queue.works = False
                    except:
                        queue.works = False
    
    if sum(queue.works for queue in queues) > 1:
        print("not sure")
    elif any(queue.works for queue in queues):
        for queue in queues:
            if queue.works:
                print(queue.name)
    else:
        print("impossible")


            

while True:
    try:
        n = int(input())
    except:
        break
    main(n)