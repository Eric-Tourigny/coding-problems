import math
import bisect


class Node:
    def __init__(self, parent: "Node | None", value: float, index: int):
        self.parent = parent
        self.value = value
        self.index = index

    def __lt__(self, other: "Node"):
        return self.value < other.value

    def __repr__(self):
        if self.parent is not None:
            return f" {self.parent} {self.value}"
        else:
            return str(self.value)



def main(numbers: list[int]):
    nodes = [ Node(None, -math.inf, -1) ]
    for index, number in enumerate(numbers):
        new_node = Node(None, number, index)
        replacement_index = bisect.bisect_left(nodes, new_node)
        new_node.parent = nodes[replacement_index - 1]

        if replacement_index == len(nodes):
            nodes.append(new_node)
        else:
            if number < nodes[replacement_index].value:
                nodes[replacement_index] = new_node

    values = []
    active_node = nodes[-1]
    while active_node.parent is not None:
        values.append(active_node.index)
        active_node = active_node.parent
    
    print(len(values))
    print(" ".join(str(value) for value in reversed(values)))




while True:
    try:
        n = int(input())
        numbers = list(map(int, input().split()))
        main(numbers)

    except EOFError as e:
        break
