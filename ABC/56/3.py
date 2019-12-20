X = int(input())
for N in range(10 ** 6):
    if N * (N + 1) // 2 >= X:
        print(N)
        exit()