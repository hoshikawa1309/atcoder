N = int(input())
A = list(map(int,input().split()))
ans = 0
for a in A:
    cnt = 0
    for i in range(1,a + 1):
        if a % 2**i == 0:
            cnt += 1
        else:
            break
    ans += cnt
print(ans)