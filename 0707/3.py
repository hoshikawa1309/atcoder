L , R = map(int,input().split())
if R - L >= 2019 or L == 0:
    print("0")
    exit()
min = 2020

for i in range(L , R):
    for j in range(i + 1 , R + 1):
        tmp_min = ( i * j) % 2019
        if tmp_min < min:
            min = tmp_min
print(min)