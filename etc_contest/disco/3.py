from pprint import pprint
H , W , K = map(int,input().split())
cake = [list(input()) for _ in range(H)]
strawberry = []
strawberry_num = 1
visited = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if cake[i][j] == "#":
            strawberry.append([i,j])
            visited[i][j] = strawberry_num
            strawberry_num += 1

for i in range(H):
    now = 0
    for j in range(W):
        if cake[i][j] == '#':
            now = visited[i][j]
        elif now != 0 and cake[i][j] == "." and visited[i][j] == 0:
            visited[i][j] = now
    now = 0

    for j in range(W-1 , -1 , -1):
        if cake[i][j] == '#':
            now = visited[i][j]
        elif now != 0 and cake[i][j] == "." and visited[i][j] == 0:
            visited[i][j] = now


for i in range(1,H):
    if visited[i][0] == 0:
        visited[i] = visited[i-1]
for i in range(H-2,-1,-1):
    if visited[i][0] == 0:
        visited[i] = visited[i+1]
for i in visited:
    print(*i)
