H , W = map(int,input().split())
matrix = [list(input()) for _ in range(H)]
delete_column = []
delete_row = []
ans = []
for row in range(H):
    if not "#" in matrix[row]:
        delete_row.append(row)
for column in range(W):
    columnFlag = True
    for row in range(H):
        if matrix[row][column] == "#":
            columnFlag = False
            break
    if columnFlag:
        delete_column.append(column)
for row in range(H):
    tmp_list = []
    for column in range(W):
        if row in delete_row or column in delete_column:
            continue
        tmp_list.append(matrix[row][column])
    if not tmp_list == []:
        ans.append(tmp_list)
for a in ans:
    print("".join(a))


