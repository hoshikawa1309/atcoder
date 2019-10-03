N , X = map(int ,input().split())
L = list(map(int,input().split()))
current = 0
cnt = 1

for val in L:
    current += val
    if current <= X:
        cnt += 1
    else:
        break
print(cnt)