N = list(input())
num = list(map(lambda x: int(x) , N))
for i in range(8):
    sum_val = num[0]
    for j in range(3):
        if i >> j & 1:
            sum_val += num[j + 1]
        else:
            sum_val -= num[j + 1]
    if sum_val == 7:
        print(num[0] , end = '')
        for j in range(3):
            if i >> j & 1:
                print("+" , end = '')
            else:
                print("-",end = '')
            print(num[j + 1] , end = '')
        print('=7')
        exit()
