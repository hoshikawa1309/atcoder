N, K = map(int, input().split())
p = list(map(int, input().split()))
Expected_val = []
for val in p:
    sum_val = (val * (val + 1)) // 2
    Expected_val.append(sum_val / val)
# print(Expected_val)

left = 0
right = K

ans = sum(Expected_val[left:right])
tmp_ans = ans
# print(ans)
for i in range(N - K):
    tmp_ans = tmp_ans - Expected_val[left + i] + Expected_val[right + i]
    if tmp_ans > ans:
        ans = tmp_ans
print(ans)
