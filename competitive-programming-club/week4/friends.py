number_of_friends, number_their_friendships = map(int, input().split())

friend_number_of_friends = [0] * number_of_friends

for _ in range(number_their_friendships):
    person1, person2 = map(int, input().split())
    friend_number_of_friends[person1 - 1] += 1
    friend_number_of_friends[person2 - 1] += 1

values = []
for i, number_of_friends in enumerate(friend_number_of_friends):
    values.append(number_of_friends - i - 1)

print(" ".join(str(value) for value in values))
