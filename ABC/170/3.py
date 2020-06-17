X, N = map(int, input().split())
p = list(map(int, input().split()))
if X not in p:
    print(X)
    exit()
judge = [False] * 102
for pi in p:
    judge[pi] = True
now = 1
Flag = False
while not Flag:
    if not judge[X - now]:
        print(X - now)
        Flag = True
    elif not judge[X + now]:
        print(X + now)
        Flag = True
    else:
        now += 1
