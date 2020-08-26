N, P = map(int, input().split())
prime = []
for i in range(2, int(P ** (1 / 2)) + 1):
    cnt = 0
    while P % i == 0:
        cnt += 1
        P //= i
    if cnt:
        prime.append([i, cnt])
if P != 1:
    prime.append([P, 1])
# print(prime)

ans = 1
for i in range(len(prime)):
    if prime[i][1] // N:
        ans *= prime[i][0]
print(ans)