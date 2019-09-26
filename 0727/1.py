A , B = map(int , input().split())
check = str((A + B) / 2 - (A + B) // 2)
#print(check)
if check[2] == "0":
    print(((A + B) // 2 ))
else:
    print("IMPOSSIBLE")
