N = int(input())
S = input()
T = input()
A = [0] * (N + 1)
B = [0] * (N + 1)
for i in range(N):
    A[i + 1] = int(A[i]) ^ int(S[i])
    B[i + 1] = int(B[i]) ^ int(T[i])
print(A)
print(B)
res = 0
s = 0
for t in range(N):
    s = max(s, t)
    if A[s] == B[t]:
        continue
    while s + 1 <= N and A[s] == A[s + 1]:
        s += 1
    if s == N:
        print(-1)
        exit()
    s += 1
    res += s - t
print(res)