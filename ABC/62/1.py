sequence = ((1, 3, 5, 7, 8, 10, 12), (4, 6, 9, 11), (2, ))

x , y = map(int, input().split())
for s in sequence:
    if x in s and y in s:
        print('Yes')
        exit()
print('No')

