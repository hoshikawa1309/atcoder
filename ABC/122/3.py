N, Q = map(int, input().split())
S = input()
AC_sum = [0] * N
sum_val = 0
for i in range(1, N):
    if S[i - 1] + S[i] == 'AC':
        sum_val += 1
    AC_sum[i] += sum_val
# print(AC_sum)
for q in range(Q):
    l, r = map(int, input().split())
    print(AC_sum[r - 1] - AC_sum[l - 1])
