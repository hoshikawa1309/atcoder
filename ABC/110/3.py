from collections import Counter
S = list(input())
T = list(input())
now = 0
idxS_dict = {}
idxT_dict = {}
for i in range(26):
    idxS_dict[chr(ord('a') + i)] = []
    idxT_dict[chr(ord('a') + i)] = []
for i in range(len(S)):
    idxS_dict[S[i]].append(i)
    idxT_dict[T[i]].append(i)

S_vals = idxS_dict.values()
T_vals = idxT_dict.values()

for val in S_vals:
    if not val in T_vals:
        print('No')
        exit()
print('Yes')

