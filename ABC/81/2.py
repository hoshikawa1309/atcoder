N = int(input())
A = list(map(float,input().split()))
ans = 0
Flag = False
while not Flag:
    for i in range(N):
        A[i] /= 2
        if not A[i].is_integer():
            Flag = True
            break
    else:
        ans += 1
print(ans)
