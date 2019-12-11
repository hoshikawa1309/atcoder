from collections import Counter
import math
N = int(input())
A = list(map(int,input().split()))
A_count = Counter(A)
count_item = list(A_count.items())
count_item.sort()
start = 1 - (N % 2)
for i in range(math.ceil(N / 2)):
    if i == 0 and N % 2 == 1:
        if count_item[i][0] == 0 and count_item[i][1] != 1:
            print("0")
            exit()
    else:
        if count_item[i][0] != i * 2 + (1 - (N % 2)) or count_item[i][1] != 2:
            print("0")
            exit()
print(2 ** (N // 2) % (10 ** 9 + 7))

