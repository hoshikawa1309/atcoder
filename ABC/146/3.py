
A , B , X = map(int,input().split())

for d in range(1,1000001):
    x = ( X - B * d ) // A
    #print(x)
    if len(str(x)) == d:
        if x > 10**9:
            print(10**9)
            exit()
        elif 10**9 >= x > 0:
            print(x)
            exit()
        else:
            continue
print("0")

