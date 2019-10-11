from pprint import pprint
N ,M = map(int,input().split())
edge = [[] for _ in range(N)]
for i in range(M):
    a , b = map(int,input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)
pprint(edge)