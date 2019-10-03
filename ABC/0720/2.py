import math
N , D = map(int , input().split())

monitoring = D * 2 + 1
print(math.ceil(N / monitoring))

