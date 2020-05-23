X = int(input())
item_num = X // 100
if item_num * 5 >= X - item_num * 100:
    print('1')
else:
    print('0')