from collections import Counter
from math import factorial
#from scipy.special import comb
def com(n , r):
    if n == 1:
        return 0
    else:
        return factorial(n) // (factorial(n - r) * factorial(r))
N = int(input())
S = []
for _ in range(N):
    s = input()
    S.append("".join(sorted(s)))
CS = Counter(S)
ans = 0
for val in CS.values():
    ans += com(val , 2 )
print(ans)