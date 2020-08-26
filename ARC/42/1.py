from collections import deque
N, M = map(int, input().split())
after = tuple(i + 1 for i in range(N))
que = deque()
flags = [True] * (N + 1)
for _ in range(M):
    a = int(input())
    que.appendleft(a)
for i in range(len(que)):
    now = que[i]
    if flags[now]:
        print(now)
        flags[now] = False

for i in range(len(after)):
    now = after[i]
    if flags[now]:
        print(now)
        flags[now] = False