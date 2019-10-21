import numpy as np
N , K = map(int,input().split())
img = [list(map(int,input().split())) for _ in range(N)]
#print(img)


for column in range(N // K):
    for row in range(N // K):
        sum = 0
        i = 0
        while i < K:
            j = 0
            while j < K:
                sum += img[i + column * K][j + row * K]
                j += 1
            i += 1
        ans = sum // (K * K)
        print(ans , end = " ")
    print()


