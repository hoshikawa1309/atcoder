X , Y = map(int,input().split())
cnt = 0
x = X
while x <= Y:
    cnt += 1
    x *=  2
print(cnt)