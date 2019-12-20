N = int(input())
A = []
for _ in range(N):
    a = int(input())
    A.append(a - 1)
Flags = [False] * N
Flags[0] = True
now = 0
cnt = 0
for _ in range(N):
    cnt += 1
    next_node = A[now]
    if next_node == 1:
        break
    if Flags[next_node]:
        print("-1")
        exit()
    Flags[next_node] = True
    now = next_node
print(cnt)
