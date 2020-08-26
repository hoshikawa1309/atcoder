H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(H):
    ans.append([0] * W)
# print(ans)
now = 0
cnt = 0
for i in range(H):
    if i % 2 == 0:
        for j in range(W):
            ans[i][j] = now + 1
            cnt += 1
            if cnt == A[now]:
                now += 1
                cnt = 0
    else:
        for j in range(W - 1, -1, -1):
            ans[i][j] = now + 1
            cnt += 1
            if cnt == A[now]:
                now += 1
                cnt = 0
for row in ans:
    print(*row, sep=' ')
