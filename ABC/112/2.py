N , T = map(int,input().split())
roots = [list(map(int,input().split())) for _ in range(N)]
min_cost = float("inf")
ans = "TLE"
for key , val in enumerate(roots):
    if val[0] < min_cost and val[1] <= T:
        min_cost = val[0]
        ans = val[0]
print(ans)