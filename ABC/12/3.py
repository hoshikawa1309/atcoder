N = int(input())
N = 2025 - N
for i in range(1 , 10):
    tmp = N / i
    if tmp.is_integer() and 0 < tmp < 10:
        print(i ,"x" , int(tmp))