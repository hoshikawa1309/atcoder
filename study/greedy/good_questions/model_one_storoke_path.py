n,m=map(int,input().split())
edge=[[] for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    a-=1;b-=1
    edge[a].append(b)
    edge[b].append(a)

def dfs(s):
    global visited
    ret=1 if all(visited) else 0
    for e in edge[s]:
        if visited[e]==True:continue
        visited[e]=True
        ret+=dfs(e)
        visited[e]=False
    return ret

ans=0
visited=[False]*n
visited[0]=True
ans+=dfs(0)

print(ans)
