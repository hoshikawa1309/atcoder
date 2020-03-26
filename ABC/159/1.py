from math import factorial
N, M = map(int, input().split())
if N >= 2:
    a = factorial(N) / factorial(2) / factorial(N - 2)
else:
    a = 0
if M >= 2:
    b = factorial(M) / factorial(2) / factorial(M - 2)
else:
    b = 0
print(int(a + b))