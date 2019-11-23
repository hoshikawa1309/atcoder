from collections import Counter
n = int(input())
v = list(map(int,input().split()))
odd = []
even = []
for i in range(n):
    if i % 2 == 0:
        even.append(v[i])
    else:
        odd.append(v[i])
cnt = 0
even_count = Counter(even)
odd_count = Counter(odd)
if len(even_count) != 1:
    work = even_count.values()
    cnt += sum(work) - max(work)
work1 = list(odd_count.values())
work1.sort(reverse=True)
work2 = list(even_count.values())
work2.sort(reverse=True)
if len(odd_count) != 1:
    cnt += sum(work) - max(work)
work1 = odd_count.keys()
work2 = even_count.keys()
if cnt == 0 and work1 == work2:
    print(n//2)
else:
    print(cnt)
