def digit_sum(n):
    n = str(n)
    S = list(map(int,n))
    return sum(S)

N , A, B = map(int,input().split())
ans = 0
for i in range(1 , N + 1):
    if A <= digit_sum(i) <= B:
       ans += i
print(ans)