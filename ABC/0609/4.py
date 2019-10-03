'''
import numpy as np
H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]
table = np.zeros((H , W))
done = np.zeros((H , W))
max = 0
print(s[0][1])

for i in range(H):
    for j in range(W):
        if s[i][j] == "#":
            continue
        if done[i][j] == 1:
            continue
        l = 0
        while j + l < W:
            if s[i][j + l] == "#":
                break
            l += 1
        for k in range(l):
            table[i][j + k] += l
            done[i][j+k] = 1
print(table)
done = np.zeros((H , W))
for j in range(W):
    for i in range(H):
        if s[i][j] == "#":
            continue
        if done[i][j] == 1:
            continue
        l = 0
        while i + l < H:
            if s[i + l][j] == "#":
                break
            l += 1
        for k in range(l):
            table[i + k][j] += l
            done[i + k][j] = 1
            if table[i + k][j] > max:
                max = table[i + k][j]

print(table)
print(int(max - 1))
'''
import numpy as np
H, W = map(int, input().split())
s = np.array([list(input()) for _ in range(H)])=="."

R = np.zeros((H,W),dtype = int)
L = np.zeros((H,W),dtype = int)
U = np.zeros((H,W),dtype = int)
D = np.zeros((H,W),dtype = int)

for i in range(H):
    U[i] = (U[i - 1] + 1) *s[i]
    D[- i - 1] = (D[-i] + 1) * s[-i-1]
for i in range(W):
    L[:,i] = (L[:,i-1] + 1) * s[:,i]
    R[:,-1-i] = (R[:,-i] + 1) * s[:,-i-1]
print(U)
print(D)
print(R)
print(L)
print(np.max(L+R+U+D - 3))