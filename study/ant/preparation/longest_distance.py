import numpy as np
N = int(input())
elem = []
for i in range(N):
    x , y = map(int,input().split())
    elem.append([x,y])
elem = np.array(elem)
max_val = 0
for i in range(N - 1):
    for j in range(i + 1 , N):
        distance = np.linalg.norm(elem[i] - elem[j])
        if max_val < distance:
            max_val = distance
print(max_val)
