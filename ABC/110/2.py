N ,M, X , Y = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
y = list(map(int,input().split()))
y.sort()
Z = y[0]
if x[-1] < y[0] and X < Z <= Y:
    print("No War")
else:
    print("War")
