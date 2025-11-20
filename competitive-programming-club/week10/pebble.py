import functools

n = int(input())
for _ in range(n):
    pebble_string = input()
    the_pebbles = tuple(char == "o" for char in pebble_string)
    SIZE = len(the_pebbles)

    @functools.cache
    def make_moves(pebbles: tuple):
        best_remaining = sum(pebbles)
        for i in range(SIZE - 2):
            if not pebbles[i] and pebbles[i + 1] and pebbles[i + 2]:
                new_locations = list(pebbles)
                new_locations[i] = True
                new_locations[i + 1] = False
                new_locations[i + 2] = False
                best_remaining = min(make_moves(tuple(new_locations)), best_remaining)
        for i in range(2, SIZE):
            if not pebbles[i] and pebbles[i - 1] and pebbles[i - 2]:
                new_locations = list(pebbles)
                new_locations[i] = True
                new_locations[i - 1] = False
                new_locations[i - 2] = False
                best_remaining = min(make_moves(tuple(new_locations)), best_remaining)

        return best_remaining

    print(make_moves(the_pebbles))