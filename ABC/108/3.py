N , K = map(int,input().split())
cnt = 0
x = 0
y = 0
for i in range(1 , N + 1):
    if i % K == 0:
        x += 1
    if i % K == K//2:
        y += 1
if K % 2 == 1:
    y = 0
print(x**3 + y**3)



'''
テストケース
3 2
'''