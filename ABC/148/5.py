N = int(input())
if N % 2 == 1:
    print("0")
    exit()


strN = str(N)
lenN = len(strN)
def cnt_zero(n , digit):
    #print(digit)
    if digit == 0:
        return 0
    alph = 0
    if n >= 5:
        alph = 1
    return n * digit + alph

ans = 0
for i in range(lenN):
    now_n = int(strN[i])
    if now_n == 0:
        now_n = 9
    #print(now_n, lenN - i - 1)
    tmp_ans = cnt_zero(now_n, lenN - i - 1)
    print(tmp_ans)
    ans += tmp_ans
print(ans)




def f(n):
    #print(n)
    if n < 2:
        return 1
    else:
        return n * f(n - 2)
print(f(N))
