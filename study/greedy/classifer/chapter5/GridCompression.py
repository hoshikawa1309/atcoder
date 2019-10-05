'''
H , W = map(int, input().split())
matrix = []
for _ in range(H):
    matrix.append(list(input()))
row_count = 0
while ['.'] * W in matrix:
    matrix.remove(['.'] * W)
    row_count += 1
column_count = 0
for i in range(W):
    if i == W - column_count:
        break
    for j in range(H - row_count):
        print("i ",i)
        print("j ",j)
        if matrix[j][i] != '.':
            break
        if j == H - 1 - row_count:
            for row in matrix:
                row.pop(i)
                print("pop")
            column_count += 1
for row in matrix:
    print("".join(row))
'''

h,w=map(int,input().split())
a=[[j for j in input()] for i in range(h)]
b=[x for x in a if "#" in x]
c = zip(*[y for y in zip(*b) if '#' in y])
for d in c:
    print("".join(d))
