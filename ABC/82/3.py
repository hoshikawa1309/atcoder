from collections import Counter
N = int(input())
A = list(map(int,input().split()))
A = Counter(A)
#print(A)
ans = 0
for key , val in A.items():
    if key > val:
        ans += val
    elif key < val:
        ans += val - key
print(ans)