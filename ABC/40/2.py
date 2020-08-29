N = int(input())
if N == 1:
    print(0)
    exit()

ans = float('inf')
for i in range(1, N):
    tmp_ans = abs(i - (N // i)) + N - (i * (N // i))
    ans = min(tmp_ans, ans)
print(ans)