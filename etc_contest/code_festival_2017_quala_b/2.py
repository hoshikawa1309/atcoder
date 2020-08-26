N, M, K = map(int, input().split())
flag = False

for j in range(M + 1):
    for i in range(N + 1):
        t = i * j + (N - i) * (M - j)
        area = M * N - t
        # area = (M - j) * i + (N - i) * j
        if area == K:
            flag = True

if flag:
    print('Yes')
else:
    print("No")