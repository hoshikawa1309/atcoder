import bisect
A , B , Q = map(int,input().split())
shrine = [int(input()) for _ in range(A)]
temple = [int(input()) for _ in range(B)]
start = [int(input()) for _ in range(Q)]

for i in range(Q):
    