from collections import Counter
N = int(input())
A = Counter(map(int, input().split()))
A = A.values()
for a in A:
    if a != 1:
        print("NO")
        exit()
print("YES")