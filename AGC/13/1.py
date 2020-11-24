N = int(input())
A = list(map(int, input().split()))
ans = 1
flag = 0
now = 0
for i in range(N - 1):
    now_A = A[i]
    next_A = A[i + 1]
    if now_A < next_A:
        if flag == -1:
            flag = 0
            ans += 1
        else:
            flag = 1
    elif now_A > next_A:
        if flag == 1:
            flag = 0
            ans += 1
        else:
            flag = -1

print(ans)