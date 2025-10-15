n, k = map(int, input().split())

count = 0
chap_count = 0
for i in range(1, n + 1):
    chap_count = chap_count * (10 ** (len(str(i))))  + i
    chap_count = chap_count % k
    if chap_count == 0:
        count += 1

print(count)