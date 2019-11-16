import math
x , y = map(int,input().split())
flag = False
MOD = 10 ** 9 + 7
for s in range(max(x,y)):
    if 2 * x - 3 * s == y:
        flag = True
        break
t = x - 2 * s
if flag:
    print(math.factorial(t+s)//(math.factorial(t) * math.factorial(s)) % MOD)
    for i in range(t+s):
else:
    print(0)