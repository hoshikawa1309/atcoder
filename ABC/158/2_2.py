N, A, B = map(int, input().split())
ans = N // (A + B) * A
N %= (A + B)
ans += min(N , A)
print(ans)