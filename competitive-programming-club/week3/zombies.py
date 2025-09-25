message = input()

if ":)" in message and ":(" in message:
    print("double agent")
elif ":)" in message:
    print("alive")
elif ":(" in message:
    print("undead")
else:
    print("machine")