n = input()

for _ in range(int(n)):
    amount, odds, favourable = input().split(" ")
    if favourable == "+":
        gain = int(amount) / 100 * int(odds)
    else:
        gain = int(amount) * 100 / int(odds)
    if gain % 1 == 0:
        print(int(gain))
    else:
        print(f"{gain:.5f}")
