def warshall_floyd():
    for middle in range(10):
        for start in range(10):
            for end in range(10):
                costs[start][end] = min(costs[start][end], costs[start][middle] + costs[middle][end])


H, W = map(int, input().split())
costs = []

for i in range(10):
    costs.append(list(map(int, input().split())))

warshall_floyd()

print(*costs, sep='\n')
ans = 0
for i in range(H):
    wall = list(map(int, input().split()))
    for num in wall:
        if num != -1:
            ans += costs[num][1]
print(ans)