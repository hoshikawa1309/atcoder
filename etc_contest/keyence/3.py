N, K, S = map(int,input().split())
for _ in range(K):
    print(S, end=" ")
for _ in range(N - K):
    if S == 10 ** 9:
        print(S - 1, end=" ")
    else:
        print(S + 1, end=" ")
