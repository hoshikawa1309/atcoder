N , M = map(int,input().split())
friendship = []
for _ in range(M):
    x , y = map(int,input().split())
    x , y = x - 1 , y - 1
    friendship.append([x,y])
ans = 0

# bit全探索で全てのパターンを列挙
for i in range(1,2**N):
    friend = []
    for j in range(N):
        if i >> j & 1:
            friend.append(j)
    flag = True

    # 全てのパターンが与えられた人間関係に存在する時Trueとする
    for j in range(len(friend) - 1):
        for k in range(j + 1 , len(friend)):
            if not [friend[j] , friend[k]] in friendship:
                flag = False
                break
    if flag:
        ans = max(len(friend) , ans)
print(ans)
