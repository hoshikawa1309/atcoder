'''
import numpy as np
import copy
S = list(int(input()))
np = np.array(len(S))
sum_val = sum(S)

while j < 3:
    work = copy.deepcopy(S)
    work[j] = work[j] * 10
    sum_val += sum(work)
'''
''' 
方針：入力文字列の桁ごとの数値と"+"を入れる組み合わせを考える。ここで"+"を挿入する、挿入しないの2bitとなる。
例
S = 123
2bitの各桁が1であるか判定し、1の時"+"を挿入
00 → 1 2 3
01 → 1+2 3
10 → 1 2+3
01 → 1+2 3
'''

S = input()
ans = 0
for i in range(2**(len(S)-1)):
    s = S
    for j in range(len(S)-1):
        if (i>>j) & 1:
            s = s[:j-len(S)+1]+'+'+s[j-len(S)+1:]
    ans += eval(s)
print(ans)
