from pprint import pprint
N = int(input())
matrix = [[0 for _ in range(9)] for _ in range(9)]
# print(matrix)
for i in range(1, N + 1):
    s = str(i)
    row = int(s[0])
    column = int(s[-1])
    if row == 0 or column == 0:
        continue
    matrix[row - 1][column - 1] += 1
# pprint(matrix)
ans = 0
for i in range(9):
    for j in range(9):
        # if i == j:
        #     ans += matrix[i][j]
        # else:
        #     ans += matrix[i][j] * matrix[j][i]
        ans += matrix[i][j] * matrix[j][i]
print(ans)

