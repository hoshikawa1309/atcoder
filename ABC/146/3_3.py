A, B, X = map(int, input().split())
ok = 0
ng = 10 ** 9 + 1
while abs(ok - ng) > 1:
    N = (ok + ng) // 2
    digit = len(str(N))
    if A * N + B * digit <= X:
        ok = N
    else:
        ng = N
print(ok)
