A , B , C ,D = map(int, input().split())
count = 0
for i in range(A,B + 1):
    flag = 0
    if i % C != 0 and i % D != 0:
        count += 1
print(count)
