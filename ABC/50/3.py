from collections import Counter
import math
N = int(input())
A = list(map(int,input().split()))
A_count = Counter(A)
Acount_keys = list(A_count.keys())
Acount_keys.sort()
#print(A_count)
now = 0

for i in range(math.ceil(N / 2)):
    key = i * 2 + (1 - N % 2)
    if Acount_keys[i] != key:
        print("0")
        exit()
    elif i == 0 and Acount_keys[i] == 0:
        if A_count[0] != 1:
            print("0")
            exit()
    elif A_count[key] != 2:
            print("0")
            exit()

print(2 ** (N // 2))


