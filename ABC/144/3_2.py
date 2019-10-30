N = int(input())
ans = float('inf')
for i in range(1,int(N**0.5) + 1):
    tmp = N / i
    if tmp.is_integer():
        if tmp == N:
            tmp_ans = N - 1
        else:
            tmp_ans = int(tmp) + i - 2
        if ans > tmp_ans:
            ans = tmp_ans
print(ans)
