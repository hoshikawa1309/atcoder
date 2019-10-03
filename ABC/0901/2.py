A , B = map(int , input().split())
ans = 1
tmp = A
if B == 1:
    print("0")
else:
    while(tmp < B):
        tmp += A - 1
        ans += 1
    print(ans)
