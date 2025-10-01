while 1:
    try:
        m = int(input())
        nodes = []
        for i in range(m):
            line = []
            for j, c in enumerate(map(int, input().split())):
                if c == 1:
                    line.append(j)
            nodes.append(line)

        def is_triangle(node):
            for other_num in node:
                for third_num in nodes[other_num]:
                    if third_num in node:
                        return True
            return False

        weak_numbers = []
        for this_num, node in enumerate(nodes):
            if not is_triangle(node):
                weak_numbers.append(this_num)

        print(" ".join(str(number) for number in weak_numbers))

    except:
        break
