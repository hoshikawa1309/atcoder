N, X = map(int, input().split())
patty = [1]
buns = [0]

for i in range(0, N):
    patty.append(patty[i] * 2 + 1)
    buns.append(buns[i] * 2 + 2)

print(patty)
print(buns)

burger_high = patty[N] + buns[N]
print("burger : ", burger_high)
print("burger/2 : ", burger_high/2)


def dfs(now_runrun, now_burger_high, dimension):
    if dimension == 0:
        return 1
    ## るんるんが一番下にいれば一つもパティは食べれない
    elif now_runrun == 1:
        return 0

    ## るんるんが真ん中にいたら、n - 1次元バーガー + 1を食べる
    elif now_runrun == now_burger_high // 2 + 1:
        return patty[dimension - 1] + 1

    ## るんるんが一番上にいたら全てのパティを食べる
    elif now_runrun == now_burger_high:
        return patty[dimension]


    next_burger = now_burger_high // 2 - 1
    next_dimension = dimension - 1

    if now_runrun <= now_burger_high // 2:
        return dfs(now_runrun - 1, next_burger, next_dimension)
    else:
        return dfs(now_runrun - (patty[next_dimension] + buns[next_dimension] + 2),
                   next_burger, next_dimension) + patty[next_dimension] + 1


print(dfs(X, burger_high, N))
