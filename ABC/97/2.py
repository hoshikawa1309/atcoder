X = int(input())
ans = 1
for b in range(2,X):
    for p in range(2,X):
        tmp_ans = b ** p
        if tmp_ans > X:
            break
        if tmp_ans > ans:
            ans = tmp_ans
print(ans)