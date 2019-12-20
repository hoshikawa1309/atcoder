N = int(input())
A = list(map(int,input().split()))
A_oddList = A[::2]
A_evenList = A[1::2]
A_oddList = A_oddList[::-1]
A_evenList = A_evenList[::-1]

if N % 2 == 1:
    A_evenList = A_evenList[::-1]
    print(*A_oddList , end = " ")
    print(*A_evenList)
else:
    A_oddList = A_oddList[::-1]
    print(*A_evenList , end = " ")
    print(*A_oddList)
