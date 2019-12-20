import numpy as np
N , A , B = map(int,input().split())
S = sorted(list(int(input()) for _ in range(N)))
if S[0] == S[-1]:
    print("-1")
    exit()
P = B / (S[-1] - S[0])
S = np.array(S)
S = P * S
Q = A - (sum(S) / len(S))
print(P , Q)