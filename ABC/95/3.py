A , B , C , X ,Y = map(int,input().split())
C_val = C * 2
ans = 0
if A + B >= C_val:
    if X >= Y:
        XYmax , XYmin = X , Y
        cmp = A
    else:
        XYmax , XYmin = Y , X
        cmp = B
    ans += XYmin * C_val
    remain = XYmax - XYmin
    if cmp >= C_val:
        ans += C_val * remain
    else:
        ans += cmp * remain
    print(ans)
else:
    print(A * X + B * Y)