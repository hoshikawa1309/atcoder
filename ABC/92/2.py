N = int(input())
D , X = map(int,input().split())
A = list(int(input()) for _ in range(N))

# 植木算的に2 ~ D日目のチョコレートを食べた日を加算し、最後に1を足す
D -= 1
ans = N
for a in A:
    ans += D // a
print(ans + X)
