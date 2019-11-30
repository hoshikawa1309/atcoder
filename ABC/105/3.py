N =int(input())
now = 0
max_list = [1]
min_list = [0]

def show_binary(now_val , now_idx):
    # print(now_val , now_idx)
    if now_idx == 0:
        print(now_val,end = "")
        return
    if now_val == 0:
        print("0", end='')
        show_binary(now_val, now_idx - 1)
    elif now_idx % 2 == 1:
        if min_list[now_idx - 1] > now_val >= min_list[now_idx]:
            print("1" , end = "")
            show_binary(now_val - (-2) ** now_idx, now_idx - 1)
        else:
            print("0" , end = '')
            show_binary(now_val, now_idx - 1)
    else:
        if max_list[now_idx - 1] < now_val <= max_list[now_idx]:
            print("1" , end = "")
            show_binary(now_val - (-2) ** now_idx, now_idx - 1)
        else:
            print("0" , end = '')
            show_binary(now_val, now_idx - 1)

for i in range(1,35):
    # iが奇数の時
    if i % 2 == 1:
        min_list.append(min_list[-1] - 2 ** i)
        max_list.append(max_list[-1])
        if min_list[i-1] >= N >= min_list[i]:
            break
    # 偶数の時
    else:
        min_list.append(min_list[-1])
        max_list.append(max_list[-1] + 2 ** i)
        if max_list[i-1] <= N <= max_list[i]:
            break
#print("max_list : ",max_list)
#print("min_list : ",min_list)
#print(i)
if 0 <= N <= 1:
    i = 0
show_binary(N,i)