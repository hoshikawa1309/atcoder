N = int(input())
cnt = [0] * (10 ** 4 + 1)
for x in range(1, 3333):
    for y in range(1, 3333):
        for z in range(1, 3333):
            check = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
            if check > 10000:
                break
            else:
                cnt[check - 1] += 1
for i in range(N):
    print(cnt[i])
