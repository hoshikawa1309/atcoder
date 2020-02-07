N, M = map(int, input().split())
if N == M == 1:
    print("1")
elif N == 1:
    print(max(0, M - 2))
elif M == 1:
    print(max(0, N - 2))
else:
    print(max(N * M - (N - 1) * 2 - (M - 1) * 2, 0))