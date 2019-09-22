'''
H , W ,A , B = map(int ,input().split())
matrix = [[0] * W for _ in range(H)]
idx = 0
k = 0
for i in range(H):
    for j in range(A):
        if k >= W:
            k -= W
        matrix[i][k] = 1
        k += 1
    k -= B - 1
flag = True
for i in matrix:
    if i.count(1) != A and i.count(0) != A:
        flag = False
for i in zip(*matrix):
    if i.count(1) != B and i.count(0) != B:
        flag = False
if flag:
    for row in matrix:
        print(*row)
else:
    print('No')
'''

H , W , A , B = map(int , input().split())
mat = [[1] * W for _ in range(H)]
for row in range(H):
    for col in range(W):
        if col < A and row < B or col >= A and row >= B:
            mat[row][col] = 0
for row in mat:
    print(*row,sep = "")
