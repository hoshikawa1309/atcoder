X = int(input())
cnt = X // 100
under = X - cnt * 100
#print(cnt)
#print(under)
if cnt * 5 >= under:
    print("1")
else:
    print("0")