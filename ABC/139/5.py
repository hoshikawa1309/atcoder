from collections import deque
from pprint import pprint
N = int(input())
nextGame = [deque()] + [deque(map(int , input().split())) for _ in range(N)]
#print(nextGame)

canPlay = [[False] * (N + 1) for _ in range(N + 1)]
#pprint(canPlay)
days = [0] * (N + 1)
que = ([i for i in range(N + 1)])

while que:
    now = que.pop()
    #print("------------------------")
    if not nextGame[now]:
        continue
    enemy = nextGame[now].popleft()
    canPlay[now][enemy] = True
    #print("now : ",now)
    #print("enemy : ",enemy)
    #pprint(canPlay)

    if canPlay[now][enemy] and canPlay[enemy][now]:
        days[now] = days[enemy] = max(days[now], days[enemy]) + 1
        que.append(now)
        que.append(enemy)
    #print("days : ",days)

for test in nextGame:
    if test:
        print("-1")
        exit(0)
print(max(days))
