N, K, S = map(int, input().split())
if S == 10 ** 9:
    etc = 1
else:
    etc = 10 ** 9
for i in range(N):
    if i < K:
        print(S, end=' ')
    else:
        print(etc, end=' ')