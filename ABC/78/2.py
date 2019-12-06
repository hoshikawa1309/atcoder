X , Y ,Z = map(int,input().split())
if X % (Z + Y) >= Z:
    print(X // (Z + Y))
else:
    print(X // (Z + Y) - 1)