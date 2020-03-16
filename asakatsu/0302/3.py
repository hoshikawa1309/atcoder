N, K = map(int,input().split())
num = []
for _ in range(N):
    num.append(list(map(int,input().split())))

for a, b in num:
    K -= b
    if K <= 0:
        print(a)
        exit()

