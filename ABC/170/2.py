X, Y = map(int, input().split())
for i in range(100):
    for j in range(100):
        if i * 2 + j * 4 == Y and i + j == X:
            print('Yes')
            exit()
print('No')