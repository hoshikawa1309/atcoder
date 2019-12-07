from collections import Counter
N =int(input())
A = Counter(list(map(int,input().split())))
B = Counter(list(map(int,input().split())))
C = Counter(list(map(int,input().split())))
A_sort = sorted(A.items())
B_sort = sorted(B.items())
C_sort = sorted(C.items())

BtoC = []
ans = 0
start_j = 0
start_k = 0
sum_val = N
for j in range(len(B_sort)):
    for k in range(start_k , len(C_sort)):
        if B_sort[j][0] >= C_sort[k][0]:
            sum_val -= C_sort[k][1]
            start_k = k + 1
        else:
            BtoC.append([B_sort[j][0] , sum_val * B_sort[j][1]])
            break
#print(BtoC)
work = 0
for i in range(len(BtoC) - 2 , -1 , -1):
    BtoC[i][1] = BtoC[i+1][1] + BtoC[i][1]
    work = BtoC[i+1][1]
#print(BtoC)
for i in range(len(A_sort)):
    for j in range(start_j , len(BtoC)):
        if A_sort[i][0] >= BtoC[j][0]:
            start_j = j + 1
        else:
            ans += A_sort[i][1] * BtoC[j][1]
            break
print(ans)