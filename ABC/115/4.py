'''
from collections import Counter
def burger(s , n):
    if n == 0:
        return s
    else:
        str = "B" + s + "P" + s + "B"
        return burger(str , n - 1)

#N , X = map(int,input().split())

for i in range(12):
    print(burger("P" , i))
    print(Counter(burger("P" , i)))


#N , X = map(int,input().split())
'''
N , X = map(int,input().split())
height = [1]
putties = [1]
for _ in range(50):
    height.append(height[-1] * 2 + 3)
    putties.append(putties[-1] * 2 + 1)
print(height)
print(putties)
def burger(n , x):
    #x は食べる量　、n は何番目のバーガーであるか
    if n == 0:
        return x
    # x <= nの時下から食べるとバンズしか食べられないため、return 0
    if x <= n:
        return 0
    hn = height[n]

    if x >= hn - n:
        return putties[n]
    # hn // 2 + 1 <= xの時真ん中より上まで食べるためn - 1番目のputtiesを全て食べることができる。
    # そのため n - 1番目のパティ + 真ん中のパティ + 中途半端なバーガー（要計算）となる
    if hn // 2 + 1 <= x:
        return putties[n - 1] + 1 + burger(n - 1, x - (hn // 2 + 1))
    return burger(n - 1,x - 1)

print(burger(N , X))