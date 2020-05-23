from collections import deque
N = int(input())
A = list(deque(map(lambda x: int(x) - 1, input().split())) for _ in range(N))
print(A)

ans = 0
change = True
while True:
    change = False
    match = [-1] * N
    for player in range(N):
        if not A[player]:
            continue
        enemy = A[player][0]
        match[player] = enemy
        if match[enemy] == player:
            A[player].popleft()
            A[enemy].popleft()
            change = True
    if not change:
        break
    ans += 1


if all(len(row) == 0 for row in A):
    print(ans)
else:
    print('-1')

