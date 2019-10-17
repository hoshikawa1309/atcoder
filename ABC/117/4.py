import numpy as np
import math
N , K = map(int,input().split())
A = list(map(int,input().split()))
'''
A.sort()
max = 0

for i in range(K + 1):
    sum = 0
    for j in range(N):
        sum += A[j] ^ i
        if sum > max:
            max = sum
print(max)
'''
count1_list = np.zeros(40)
count0_list = np.zeros(40)
for a in A:
    binary = bin(a)
    binary = binary[::-1]
    for i in range(len(binary) - 2):
        if binary[i] == "1":
            count1_list[i] += 1
        else:
            count0_list[i] += 1

ans = []
for i in range(40):
    if count1_list[i] < count0_list[i]:
        ans.append(1)
    else:
        ans.append(0)
print(ans)


