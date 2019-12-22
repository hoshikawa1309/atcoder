A = int(input())
B = int(input())
lst = [A,B]
for i in range(1,4):
    if not i in lst:
        print(i)
        exit()