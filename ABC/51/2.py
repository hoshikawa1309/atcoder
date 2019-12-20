K , S = map(int,input().split())
ans = 0
for i in range(K + 1):
    for j in range(K + 1):
        k = S - i - j
        if K >= k >= 0:
            ans += 1
print(ans)
