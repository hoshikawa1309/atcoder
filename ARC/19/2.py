A = input()
len_A = len(A)
diff_cnt = 0
palindrome_cnt = 0
for i in range(len_A // 2):
    if A[i] != A[len_A - i - 1]:
        diff_cnt += 1
if len_A % 2 == 0:
    if diff_cnt == 1:
        palindrome_cnt += 2
else:
    if diff_cnt == 0:
        palindrome_cnt += 25
    elif diff_cnt == 1:
        palindrome_cnt += 2
ans = len_A * 25 - palindrome_cnt
print(ans)