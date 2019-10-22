K , S = map(int,input().split())
cnt = 0
for x in range(K + 1):
    for y in range(K + 1):
        if x + y > S:
            continue
        z = S - x - y
        if z <= K:
            cnt += 1
print(cnt)