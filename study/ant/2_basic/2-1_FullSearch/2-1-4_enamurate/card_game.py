import itertools
import math
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
victory = 0
for a in A:
    b_tmp = B.pop(0)
    B.append(b_tmp)
    a_w = 0
    b_w = 0
    for b in B:
        if a > b:
            a_w += 1
        else:
            b_w += 1
    if a_w > b_w:
        victory += 1

print(victory / (len(list(itertools.product(A,B))) // N))