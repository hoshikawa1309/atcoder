'''
N , Y = map(int , input().split())
for y in range(N + 1):
    z = - N / 9 + Y / 9000 - 4 * y / 9
    tmp_z = z - int(z)
    if str(tmp_z)[2] != "0":
        continue
    else:
        z = int(z)
    x = 5 * N / 4 - Y / 4000 + 5 * z / 4
    tmp_x = x - int(x)
    if str(tmp_x)[2] != "0":
        continue
    else:
        x = int(x)

    if x >= 0 and y >= 0 and z >= 0:
        print("------------")
        print(x)
        print(y)
        print(z)
        print("------------")
    if x + y + z == N and 1000 * x + 5000 * y + 10000 * z == Y and 2000 >= x >= 0 and 2000 >= z >= 0:#and y >= 0 and z >= 0:
        print(z,y,x)
        exit(0)
print("-1 -1 -1")
'''
N , Y = map(int , input().split())
for k1 in range(N + 1):
    for k5 in range(N + 1 - k1):
        k10 = N - k1 - k5
        if k1 + k5 + k10 == N and 1000 * k1 + 5000 * k5 + 10000 * k10 == Y and k10 >= 0:
            print(k10 , k5 , k1)
            exit(0)
print("-1 -1 -1 ")
