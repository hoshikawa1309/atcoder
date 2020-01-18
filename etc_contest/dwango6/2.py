N = int(input())
x = list(map(int,input().split()))
MOD = 10 ** 9 + 7
fact = 1
for i in range(1 , N):
    fact *= i
    fact %= MOD

sum_val = 0
expected_val = 0
for i in range(N - 1):
    sum_val += (x[-1] - x[i])
    expected_val += sum_val / (N - 1)
print(int(expected_val * fact % MOD))