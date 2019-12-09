from collections import Counter
N = int(input())
A = list(map(int,input().split()))
MOD = 10 ** 9 + 7
ans = 0
bit_matrix = [[0] * N for _ in range(61)]
for i in range(len(A)):
    n = 0
    while 2 ** n <= A[i]:
        if A[i] >> n & 1:
            bit_matrix[n][i] = 1
        n += 1
#print(bit_matrix)
#bit_matrix_T = []
'''
for j in range(60):
    tmp = []
    for i in range(N):
        tmp.append(bit_matrix[i][j])
    bit_matrix_T.append(tmp)
'''
#print(bit_matrix_T)
for i in range(len(bit_matrix)):
    tmp = Counter(bit_matrix[i])
    a = list(tmp.values())
    if len(a) == 2:
        ans += (2 ** i) * a[0] * a[1]
        ans %= MOD
print(ans)
