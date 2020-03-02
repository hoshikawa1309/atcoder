N, L = map(int,input().split())
S = list(input() for _ in range(N))
S.sort()
print("".join(S))