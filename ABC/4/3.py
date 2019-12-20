N = int(input())
N = N % 6
add_num = 2
for i in range(6):
    if i == N:
        print("1" , end = "")
        add_num = 1
    else:
        print(i + add_num, end = "")