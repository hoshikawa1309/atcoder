N, T = map(int, input().split())
A_times = []
B_times = []
diff_time = []
for _ in range(N):
    a, b = map(int, input().split())
    A_times.append(a)
    B_times.append(b)
    diff_time.append(a - b)
if sum(B_times) > T:
    print(-1)
    exit()
diff_time.sort()
now = sum(B_times)
ans = N
for diff in diff_time:
    if now + diff > T:
        break
    now += diff
    ans -= 1
print(ans)
