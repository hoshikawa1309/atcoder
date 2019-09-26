'''
import numpy as np
import math

N , M = map(int, input().split())
A = list(map(int , input().split()))
np_list = np.array(A)
#print(A)
for _ in range(M):
    #print(np_list)
    max_index = np_list.argmax()
    #print(max_index)
    np_list[max_index] = np_list[max_index] / 2
A = list(map( lambda x : math.floor(x) , A ))
print(sum(np_list))
'''
import math
import heapq
N , M = map(int, input().split())
A = list(map(int , input().split()))
A = list(map( lambda x : x * (-1) , A ))
heapq.heapify(A)
for _ in range(M):
    tmp = heapq.heappop(A) * (-1) / 2
    heapq.heappush(A,tmp * (-1))
A = list(map( lambda x : x * (-1) , A ))
A = list(map( lambda x : math.floor(x) , A ))
print(sum(A))
