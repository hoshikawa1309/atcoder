from math import ceil, floor
N = int(input())
A = list(map(int, input().split()))
average = sum(A) / N
floor_A = floor(average)
ceil_A = ceil(average)
floor_sum = 0
ceil_sum = 0
for a in A:
    floor_sum += (a - floor_A) ** 2
    ceil_sum += (a - ceil_A) ** 2
print(min(ceil_sum, floor_sum))