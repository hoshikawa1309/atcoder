import numpy as np

N, D = map(int , input().split())
X = [list(map(int , input().split())) for _ in range(N)]
X = np.array(X)
cnt = 0
for i in range(N - 1):
    for j in range(i + 1 , N):
        dis = np.linalg.norm(X[i] - X[j])
        if dis.is_integer():
            cnt += 1
print(cnt)