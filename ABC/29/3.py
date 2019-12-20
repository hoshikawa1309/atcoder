def Base_10_to_n(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    if out == "":
        return 0
    else:
        return out
N = int(input())
lst = ["a","b","c"]
for i in range(3 ** N):
    base3_num = str(Base_10_to_n(i , 3)).zfill(N)
    #print(base3_num)
    for i in range(N):
        idx = int(base3_num[i])
        print(lst[idx],end = '')
    print()

