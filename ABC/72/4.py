N = int(input())
P = list(map(int,input().split()))
cnt = 0
is_continue = False
for i in range(N):
    if (i + 1) == P[i]:
        cnt += 1
        if is_continue:
            cnt -= 1
            is_continue = False
        else:
            is_continue = True
    else:
        is_continue = False
print(cnt)