from collections import Counter
a = Counter(map(int,input().split()))
if 2 in a.values():
    print("Yes")
else:
    print("No")