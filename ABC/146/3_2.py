import math
A , B , X = map(int,input().split())
ans = 10**9 // 2
diff = ans
digit_ans = len(str(ans))
while not A * ans + B * digit_ans <= X < A * (ans+1) + B * len(str(ans+1)):
    diff = max(diff // 2 , 1)
    if A * ans + B * digit_ans > X:
        ans -= diff
    else:
        ans += diff
    digit_ans = len(str(ans))
    #print(ans)
    if ans >= 10 ** 9:
        print(10**9)
        exit()
    elif ans <= 0:
        print("0")
        exit()
print(ans)
