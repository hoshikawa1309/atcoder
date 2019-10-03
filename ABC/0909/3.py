N = int(input())
B = list(map(int,input().split()))
A = []
B.reverse()
for i in range(N):
    #print(i)
    if i == 0:
        A.append(B[i])
    elif i == N - 1:
        A.append(B[i - 1])
    else:
        A.append(min(B[i] , B[i - 1]))
print(sum(A))
