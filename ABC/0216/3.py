def gcd(x , y):
    while y != 0:
        x , y = y , x % y
    return x

N = int(input())
A = list(map(int,input().split()))
ans = gcd(A[0],A[1])
for i in range(2 , N):
    ans = gcd(ans,A[i])
print(ans)