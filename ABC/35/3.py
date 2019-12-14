N , Q = map(int,input().split())
row = [0] * (N + 1)
for _ in range(Q):
    l , r = map(int,input().split())
    l -= 1
    row[l] += 1
    row[r] -= 1
now = 0
for i in range(N):
    now += row[i]
    row[i] = now
    print(row[i] % 2 , end = "")
print()