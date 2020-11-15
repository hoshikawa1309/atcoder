N, W = map(int, input().split())
times = [0] * (2 * 10 ** 5 + 5)
for _ in range(N):
    s, t, p = map(int, input().split())
    times[s] += p
    times[t] += -p

sum_val = 0
for t in times:
    sum_val += t
    if sum_val > W:
        print('No')
        exit()
print('Yes')