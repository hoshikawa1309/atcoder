N = int(input())
A = list(map(int , input().split()))
blue_ans = bin(A[0])
red_ans = bin(A[1])
print(blue_ans)
for i in range(2,N):
    tmp = bin(A[i])
    print(tmp)
    if i % 2 == 0:
        blue_ans = bin(tmp) ^ blue_ans
    else:
        red_ans = bin(tmp) ^ red_ans
print(int(blue_ans[2:] , 2) +int(red_ans[2:] , 2) )
