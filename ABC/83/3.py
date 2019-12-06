X , Y = map(int,input().split())
now = X
ans = 0
while now <= Y:
    ans += 1
    now *= 2
print(ans)