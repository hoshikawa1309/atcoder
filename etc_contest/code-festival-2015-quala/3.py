N, T = map(int, input().split())
A_times = []
B_times = []
for _ in range(N):
    a, b = map(int, input().split())
    A_times.append(a)
    B_times.append(b)

if sum(B_times) < T:
    print(-1)
    exit()

