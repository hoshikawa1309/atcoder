N , K = map(int,input().split())
S = list(int(input()) for _ in range(N))
if 0 in S:
    print(N)
    exit()
right = 0
left = 0
ans = 0
tmp_ans = 0
sum_val = 1

while right < N:
    if S[right] * sum_val <= K:
        sum_val *= S[right]
        right += 1
        tmp_ans += 1

    else:
        sum_val = max(sum_val // S[left] , 1)
        left += 1
        tmp_ans = max(0,tmp_ans - 1)
        right = max(right,left)


    if tmp_ans > ans:
        ans = tmp_ans
print(ans)