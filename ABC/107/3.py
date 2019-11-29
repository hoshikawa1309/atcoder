N , K = map(int,input().split())
x = list(map(int,input().split()))
ans = float("inf")
for i in range(N - K + 1):
    #x = x[i : i + K]

    if x[i + K - 1] <= 0:
        tmp_min = abs(x[i])
    elif 0 <= x[i]:
        tmp_min = abs(x[i + K - 1])
    else:
        PassTwice = min(abs(x[i + K - 1]) ,abs(x[i])) * 2
        PassOnce = max(abs(x[i + K - 1]) ,abs(x[i]))
        tmp_min = PassTwice + PassOnce
    if tmp_min < ans:
        ans = tmp_min
print(ans)