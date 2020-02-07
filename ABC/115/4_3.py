N, X = map(int, input().split())
pattis = [1]
buns = [0]

for i in range(N):
    pattis.append(pattis[i] * 2 + 1)
    buns.append(buns[i] * 2 + 2)

# print(pattis)
# print(buns)

def dfs(n , x):
    ## 終了条件
    if n == 0:
        return 1


    ## 0次元バーガー前に終了する条件
    burger_high = pattis[n] + buns[n]
    if x == 1:
        return 0
    elif x == burger_high:
        return pattis[n - 1] * 2 + 1
    elif x == burger_high // 2 + 1:
        return pattis[n - 1] + 1

    ## 再帰的に探索を続ける
    if 1 < x <= burger_high // 2:
        return dfs(n - 1, x - 1)
    elif burger_high // 2 < x < burger_high:
        return dfs(n - 1, x - (pattis[n - 1] + buns[n - 1] + 2)) + pattis[n - 1] + 1


print(dfs(N, X))