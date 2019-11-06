N = int(input())
points = list(map(int,input().split()))
dp = [[0] * (N + 1) for _ in range(sum(points) + 1)]
def solve(i , idx):
    if i in ans or idx == N:
        return
    ans.append(i)
    solve(i + points[idx] , idx + 1)
    solve(i, idx + 1)

solve(0 , 0)
print(len(ans))