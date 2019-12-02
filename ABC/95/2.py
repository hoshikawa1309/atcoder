N , X = map(int,input().split())
m = list(int(input()) for _ in range(N))
m.sort()
print((X - sum(m)) // m[0] + N)