'''
N = int(input())
present = []
for _ in range(N):
    w , h = map(int,input().split())
    present.append([w , h])

present.sort(reverse=True)
present.sort(reverse=True , key=lambda x: x[1] )

ans = 1
now_box = present[0]
for i in range(1,N):
    if now_box[0] > present[i][0] and now_box[1] > present[i][1]:
        now_box = present[i]
        ans += 1
print(ans)

'''

## DPでとく
## WAとTLE祭り泣
from functools import lru_cache
import sys
sys.setrecursionlimit(10 ** 6)
N = int(input())
present = []
for _ in range(N):
    w , h = map(int,input().split())
    present.append([w , h])
present.sort(reverse=True)
present.sort(reverse=True, key=lambda x: x[1])

@lru_cache(maxsize=None)
def solve(i , W , H):
    if i == N:
        return 0
    if present[i][0] >= W or present[i][1] >= H:
        ret_val = solve(i+1,W ,H)
    else:
        ret_val = max(solve(i+1,W,H) , solve(i+1,present[i][0],present[i][1]) + 1)
    return ret_val

print(solve(1 , present[0][0],present[0][1]) + 1)
