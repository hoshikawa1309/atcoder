N , M = map(int,input().split())
if M <= N * 2:
    ans = M // 2
else:
    nokori = (M - (N * 2))
    #print(nokori)
    ans = N + nokori // 4
print(ans)
