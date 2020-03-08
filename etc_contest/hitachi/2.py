A, B , M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = min(a) + min(b)
for _ in range(M):
    x, y, c = map(int,input().split())
    tmp_ans = a[x - 1] + b[y - 1] - c
    if tmp_ans < ans:
        ans = tmp_ans
print(ans)