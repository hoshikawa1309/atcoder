N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
if N < 3:
    print('0')
    exit()
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if L[i] == L[j] or L[j] == L[k] or L[i] == L[k]:
                continue
            if L[k] < L[i] + L[j]:
                ans += 1
print(ans)