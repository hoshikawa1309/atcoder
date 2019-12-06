from collections import Counter
N , K = map(int,input().split())
A = Counter(list(map(int,input().split())))
valList = list(A.values())
valList.sort(reverse=True)
print(sum(valList[K:]))