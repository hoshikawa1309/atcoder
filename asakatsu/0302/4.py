N = int(input())
S = list(list(input()) for _ in range(N))
S.sort(key=lambda x: x[-1])
print(S)
