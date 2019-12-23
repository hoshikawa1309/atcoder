N = int(input())
if N % 2 == 1:
    print("0")
    exit()

ans = 0
n = 1
N //= 2
while N > 1:
    ans += N // 5
    N //= 5
    print(N)
print(ans)