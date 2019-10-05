N , M = map(int,input().split())
edge = []
for _ in range(M):
    a ,b = map(int ,input().split())
    a , b = a - 1 , b - 1
    edge.append((a,b))

def root(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = root(parent[a])
        return parent[a]

def is_same(a,b):
    return root(a) == root(b)

def unite(a , b):
    ra = root(a)
    rb = root(b)
    if ra == rb:
        return
    parent[ra] = rb

ans = 0
for i in range(M):
    parent = [k for k in range(N)]
    for j , e in enumerate(edge):
        if j == i:
            continue
        a , b = e
        unite(a , b)
    a , b = edge[i]
    if not is_same(a , b):
        ans += 1
print(ans)
