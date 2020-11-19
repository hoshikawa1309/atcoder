A = input()
for i in range(10, 1000000):
    sum_val = 0
    str_i = str(i)
    for j in range(len(str_i)):
        sum_val += i ** (len(str_i) - 1 - j) * int(str_i[j])
        if sum_val > int(A):
            break
    else:
        if sum_val == int(A):
            print(i)
            exit()
print(-1)
