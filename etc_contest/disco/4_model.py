M = int(input())
keta = 0
count_sum = 0
for _ in range(M):
    d,c= map(int,input().split(' '))
    keta += c
    count_sum += d*c
print("keta : ",keta)
print("count_sum : ", count_sum)
if 9 < count_sum:
    print(keta-1 + (count_sum-1)//9)
else:
    print(keta-1)