N, K = map(int, input().split())
A = tuple(int(input()) for _ in range(N))
flag = True
start = 0
ans = 0
while start + K <= N:
    for i in range(start, start + K - 1):
        if A[i] >= A[i + 1]:
            flag = False
            break
    else:
        ans += 1
        now = start + K - 1
    if flag:
        while now < N - 1:
            if A[now] < A[now + 1]:
                ans += 1
                now += 1
            else:
                break
        start = now - 1
    else:
        flag = True
    start += 1
print(ans)

