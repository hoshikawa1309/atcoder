from pprint import pprint
from scipy.sparse.csgraph import floyd_warshall
from itertools import permutations

N , M , R = map(int ,input().split())
r = list(map(int , input().split()))
cost = [[0] * N for i in range(N)]
for _ in range(M):
    a,b,c = (list(map(int,input().split())))
    a , b = a - 1,b - 1
    cost[a][b] = c
    cost[b][a] = c
    #pprint(cost)
#pprint(cost)
cost = floyd_warshall(cost)
#pprint(cost)
ans = float("inf")

for i in permutations(r):
    #print("i : ",i)
    tmp_ans = 0
    for j in range(R - 1):
        #print("j : ",j)
        tmp_ans += cost[i[j] - 1][i[j + 1] - 1]
    ans = min(ans , tmp_ans)
print(int(ans))
