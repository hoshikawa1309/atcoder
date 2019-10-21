n , m = map(int , input().split())
edge = [[] for _ in range(n) ]
#print(edge)
for _ in range(m):
    a , b = map(int , input().split())
    a -= 1 ; b -= 1
    edge[a].append(b)
    edge[b].append(a)
print(edge)

def DFS(s):
    global visited
    #ret=1 if all(visited) else 0
    if all(visited):
        ret = 1
    else:
        ret = 0
    for e in edge[s]:
        #print("e",e)
        if visited[e] == True:
            continue
        visited[e] = True
        ret += DFS(e)
        visited[e] = False
    return ret


visited = [False] * n
visited[0] = True
ans = DFS(0)
print(ans)
