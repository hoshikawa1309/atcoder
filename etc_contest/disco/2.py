N = int(input())
A = list(map(int,input().split()))
previous = 0
following = sum(A)
ans = float("inf")
for a in A:
    previous += a
    following -= a
    tmp_ans = abs(previous - following)
    if ans > tmp_ans:
        ans = tmp_ans
print(ans)