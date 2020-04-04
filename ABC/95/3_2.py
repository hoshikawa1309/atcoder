A, B, C, X, Y = map(int, input().split())
ans = 0
ans = A * X + B * Y
tmp_ans = C * (X + Y) * 2
if tmp_ans < ans:
    ans = tmp_ans

tmp_ans = (Y * 2) * C
tmp_ans += max((X - Y), 0) * A
if tmp_ans < ans:
    ans = tmp_ans

tmp_ans = (X * 2) * C
tmp_ans += max((Y - X), 0) * B
if tmp_ans < ans:
    ans = tmp_ans
print(ans)