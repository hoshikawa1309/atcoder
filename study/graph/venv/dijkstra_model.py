n,m,s,t=map(int,input().split())
uvab=[map(int,input().split()) for i in range(m)]
inf=10**20
c1=[[] for i in range(n)]
c2=[[] for i in range(n)]
for u,v,a,b in uvab:
    c1[u-1].append((v-1,a))
    c1[v-1].append((u-1,a))
    c2[u-1].append((v-1,b))
    c2[v-1].append((u-1,b))
from heapq import heappop,heappush
def dij(c,N,start):
    d=[inf]*N
    d[start]=0
    prev=[-1]*N
    q=[]
    heappush(q,(0,start))
    while len(q)>0:
        u=heappop(q)[1]
        for v,w in c[u]:
            if w<inf:
                temp=d[u]+w
                if d[v]>temp:
                    d[v]=temp
                    prev[v]=u
                    heappush(q,(d[v],v))
    return d
d1=dij(c1,n,s-1)
d2=dij(c2,n,t-1)
print(d1)
print(d2)
r=[0]*n
for i in range(n):
    r[-i-1]=max(r[-i],10**15-int(d1[-i-1])-int(d2[-i-1]))
print(*r,sep='\n')

