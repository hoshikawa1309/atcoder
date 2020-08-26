def change(x, char):
    if x == 1:
        ans[3][3] = char
    elif x == 2:
        ans[2][2] = char
    elif x == 3:
        ans[2][4] = char
    elif x == 4:
        ans[1][1] = char
    elif x == 5:
        ans[1][3] = char
    elif x == 6:
        ans[1][5] = char
    elif x == 7:
        ans[0][0] = char
    elif x == 8:
        ans[0][2] = char
    elif x == 9:
        ans[0][4] = char
    elif x == 0:
        ans[0][6] = char



a, b = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
ans = [['x', ' ', 'x', ' ', 'x', ' ', 'x'],
       [' ', 'x', ' ', 'x', ' ', 'x'],
       [' ', ' ', 'x', ' ', 'x'],
       [' ', ' ', ' ', 'x']]
# print(ans[0][0])

for i in range(10):
    if i in p:
        change(i, '.')
    if i in q:
        change(i, 'o')

for row in ans:
    print(*row)

