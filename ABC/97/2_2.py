X = int(input())
ans = 1
for b in range(1, X):
    for p in range(2, X):
        tmp = b ** p
        if tmp > X:
            break
        if ans < tmp:
            ans = tmp
print(ans)