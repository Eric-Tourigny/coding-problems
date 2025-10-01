def to_hex(value):
    match value:
        case "F":
            return 15
        case "E":
            return 14
        case "D":
            return 13
        case "C":
            return 12
        case "B":
            return 11
        case "A":
            return 10
    return int(value)

while True:
    rows, columns = map(int, input().split())
    if rows == 0 and columns == 0:
        break

    values = []
    for row in range(rows):
        values.append(list(map(to_hex, input())))


    def move_up(value):
        return not value & 0b1000

    def move_right(value):
        return not value & 0b0100

    def move_down(value):
        return not value & 0b0010

    def move_left(value):
        return not value & 0b0001

    open = []

    for i, cell in enumerate(values[0]):
        if move_up(cell):
            open.append((0, i))

    for i, cell in enumerate(values[-1]):
        if move_down(cell):
            open.append((rows - 1, i))

    for i, row in enumerate(values):
        if move_left(row[0]):
            open.append((i, 0))

    for i, row in enumerate(values):
        if move_right(row[-1]):
            open.append((i, columns - 1))

    end = open[1]

    visited = [[0] * columns for _ in range(rows)]
    
    double_visit_flag = False

    def go_to_next(current, last):
        if visited[current[0]][current[1]] == 0:
            visited[current[0]][current[1]] = 1
            value = values[current[0]][current[1]]

            if move_up(value) and current[0] != 0:
                new_node = (current[0] - 1, current[1])    
                if new_node != last:
                    go_to_next(new_node, current)

            if move_down(value) and current[0] != rows - 1:
                new_node = (current[0] + 1, current[1])
                if new_node != last:
                    go_to_next(new_node, current)

            if move_right(value) and current[1] != columns - 1:
                new_node = (current[0], current[1] + 1)
                if new_node != last:
                    go_to_next(new_node, current)

            if move_left(value) and current[1] != 0:
                new_node = (current[0], current[1] - 1)
                if new_node != last:
                    go_to_next(new_node, current)

        else:
            global double_visit_flag
            double_visit_flag = True

    go_to_next(open[0], None)

    if not visited[end[0]][end[1]]:
        print("NO SOLUTION")
    elif not all(all(row) for row in visited):
        print("UNREACHABLE CELL")
    elif double_visit_flag:
        print("MULTIPLE PATHS")
    else:
        print("MAZE OK")