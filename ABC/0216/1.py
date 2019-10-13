A , B = map(int,input().split())
x = B / A
if x.is_integer():
    print(A + B)
else:
    print(B - A)