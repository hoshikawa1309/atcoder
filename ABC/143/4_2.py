N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1 ,N):
            a = L[i]
            b = L[j]
            c = L[k]
            if a < b + c and b < a + c and c < a + b:
                ans += 1
            else:
                break
print(ans)