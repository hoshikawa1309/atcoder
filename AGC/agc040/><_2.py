import numpy as np
S = list(input())
S_len = len(S)
num_lst = np.zeros(S_len + 1)
for i in range(S_len):
    if S[i] == "<":
        num_lst[i + 1] = max(num_lst[i] + 1, num_lst[i + 1])


for i in range(S_len - 1, -1 , -1):
    if S[i] == ">":
        num_lst[i] = max(num_lst[i], num_lst[i + 1] + 1)
print(int(np.sum(num_lst)))