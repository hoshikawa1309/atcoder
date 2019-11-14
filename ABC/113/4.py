# H = 100 , W = 8なので多分全探索するのかな？

H , W , K = map(int,input().split())
lst = [[0] * (W-1) for _ in range(W)]
for i in range(W - 1):
    lst[i][i] = 1
print(lst)