W , H ,x , y = map(int,input().split())
'''
horizon = min(W * y , W * (H - y))
vertical = min(H * x , H * (W - x))
# 直線上に存在すれば三角形の面積
if x == W or y == H or x == 0 or y == 0:
    print("{:.6f}".format((W * H) / 2) , end = ' ')
    print("0")
# 直線上にない時、長方形の面積
else:
    print('{:.6f}'.format(max(horizon , vertical)) , end = ' ')
    if horizon == vertical:
        print("1")
    else:
        print("0")
'''

print("{:.6f}".format(W * H /2) , end = ' ')
if x + x  == W and y + y == H:
    print('1')
else:
    print("0")