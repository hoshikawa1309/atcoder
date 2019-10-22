N = int(input())
meets = [int(input()) for _ in range(N)]
ans = float("inf")
for bit in range(1 , 2 ** N):
    right = 0
    left = 0
    for idx in range(N):
        if bit >> idx & 1:
            right += meets[idx]
        else:
            left += meets[idx]
    tmp_ans = max(right , left)
    if tmp_ans < ans:
        ans = tmp_ans
print(ans)