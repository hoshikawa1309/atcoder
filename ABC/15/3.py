N , K = map(int,input().split())
T = list(list(map(int,input().split())) for _ in range(N))
for i in range(K ** N):
    check_num = T[0][i // K]
    for j in range(1 , N):
        check_num ^= T[j][i % K]
    if check_num == 0:
        print("Found")
        exit()
print("Nothing")