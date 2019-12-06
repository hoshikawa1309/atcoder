A , B = map(int,input().split())
cnt = 0
for i in range(A , B + 1):
    check = list(str(i))
    if check == check[::-1]:
        cnt += 1
print(cnt)