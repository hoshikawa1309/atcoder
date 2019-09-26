import heapq
import copy
N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
list = A
list = sorted(list)
max = list[-1]
second_max = list[-2]
cnt = A.count(max)
for i in range(N):
    if A[i] == max and  cnt == 1:
        print(second_max)
    else:
        print(max)

    '''
    if elem != "":
        heapq.heappush(A,(-1) * elem)
    heapq.heapify(A)
    elem = (-1) * heapq.heappop(list)
    print(elem)
    
    list = copy.deepcopy(A)
    del list[i]
    heapq.heapify(list)
    print((-1) * heapq.heappop(list))
    '''
    '''
    list = A[:i] + A[i + 1:]
    heapq.heapify(list)
    print((-1) * heapq.heappop(list))
    '''



