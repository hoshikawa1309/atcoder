import heapq
N , M = map(int ,input().split())
a = list(map(int ,input().split()))

heapq.heapify(a)
lst = []
for i in range(M):
    b , c = map(int ,input().split())
    lst.append([b, c])
lst.sort(reverse = True , key = lambda x: x[1])
#print(lst)
for i in range(M):
    for _ in range(lst[i][0]):
        if lst[i][1] <= a[0]:
            break
        heapq.heappop(a)
        heapq.heappush(a,lst[i][1])
print(sum(a))