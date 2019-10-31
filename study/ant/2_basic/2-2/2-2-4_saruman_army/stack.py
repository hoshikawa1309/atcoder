import bisect
n = int(input())
#w = list(int(input()) for _ in range(n))
lst = [int(input())]
cnt = 1
for i in range(1,n):
    x = int(input())
    min_idx = bisect.bisect_left(lst,x)
    if min_idx == len(lst):
        lst.append(x)
    else:
        lst[min_idx] = x
print(len(lst))