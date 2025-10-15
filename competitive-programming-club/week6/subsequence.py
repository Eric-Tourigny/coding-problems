n = int(input())
numbers = list(map(int, input().split()))

class Seq:
    def __init__(self, value):
        self.max = value
        self.values = [value]
    
    def add(self, value):
        self.max = value
        self.values.append(value)

def search(sequences: list[Seq], low, high, value):
    if low == high:
        return low
    
    mid = (low + high) // 2
    if sequences[mid].max < value:
        return search(sequences, low, mid, value)
    else:
        return search(sequences, mid + 1, high, value)
    

size = 0
sequences: list[Seq] = []

for i, value in enumerate(numbers):
    j = search(sequences, 0, size, value)
    if j == size:
        size += 1
        sequences.append(Seq(value))
    else:
        
        sequences[j].add(value)
    
print(len(sequences))

for seq in sequences:
    print(" ".join(str(x) for x in seq.values))