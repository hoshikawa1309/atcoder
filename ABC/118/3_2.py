def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N = int(input())
l = list(map(int, input().split()))
ans = l[0]
for i in range(1, N):
    ans = gcd(ans, l[i])
print(ans)