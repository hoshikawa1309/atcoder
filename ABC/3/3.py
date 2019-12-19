N , K = map(int,input().split())
R = list(map(int,input().split()))
R.sort()
work_R = R[N - K:]
ans = 0
for val in work_R:
    ans = (ans + val) / 2
print(ans)