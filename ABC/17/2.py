X = list(input())
while X:
    if len(X) >= 2 and X[-1] == 'h' and X[-2] == 'c':
        for _ in range(2):
            X.pop(-1)
    elif X[-1] == 'o' or X[-1] == 'k' or X[-1] == 'u':
        X.pop(-1)
    else:
        print('NO')
        exit()
print('YES')

