from itertools import groupby
ans = premax = 0
S = groupby(input())
#for key , s in S:
#    print(key ,list(s))
for k, g in S:
    #enumerateの第二引数はインデックスの開始数値
    for c, _ in enumerate(g, 1):
        ans += c
        print("c : ", c)
        print("ans : ",ans)
    if k == '>':
        ans -= min(c, premax)
    premax = c
print(ans)