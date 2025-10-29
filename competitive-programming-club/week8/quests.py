values = []

class Node:
    def __init__(self, e, g):
        self.e = e
        self.g = g
        self.left: Node | None = None
        self.right: Node | None = None
    
    def __lt__(self, other: "Node"):
        if self.e == other.e:
            return self.g < other.g
        return self.e < other.e

class Tree:
    def __init__(self):
        self.head: Node | None = None
    
    def add(self, e, g):
        new_node = Node(e, g)
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node != None:
                if (new_node < current_node):
                    if current_node.left == None:
                        current_node.left = new_node
                        current_node = None
                    else:
                        current_node = current_node.left


                else:
                    if current_node.right == None:
                        current_node.right = new_node
                        current_node = None
                    else:
                        current_node = current_node.right   
            


n = int(input())
for i in range(n):

    command, *array = input().split()
    if command == "add":
        E, G = map(int, array)
        heapq.heappush(values, (E, G))
    if command == "query":
        energy = int(array[0])
        E, G = heapq.heappop(values)
        print(G)
