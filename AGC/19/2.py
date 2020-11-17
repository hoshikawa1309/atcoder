from collections import Counter
A = list(Counter(input()).values())
ans = 1
for i in range(len(A) - 1):
    for j in range(i + 1, len(A)):
        ans += A[j] * A[i]
print(ans)