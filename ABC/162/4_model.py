N = int(input())
S = input()
r = g =  b = 0
for s in S:
    if s == 'R':
        r += 1
    elif s == 'G':
        g += 1
    else:
        b += 1

double = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        k = (j - i) * 2 + i
        if k >= N:
            continue
        if S[i] != S[j] and S[j] != S[k] and S[i] != S[k]:
            double += 1
print(r * g * b - double)