'''
N = int(input())
book = []
for i in range(N):
    s , p = input().split()
    book.append([s,int(p),i + 1])
if N == 1:
    print(1)
    exit()
book.sort()
tmp_name = book[0][0]
tmp_list = []
tmp_list.append(book[0])

for i in range(1,N):
    if book[i][0] == tmp_name:
        tmp_list.append(book[i])
    else:
        tmp_list.sort(key = lambda x: -x[1])
        for j in tmp_list:
            print(j[2])
        tmp_name = book[i][0]
        tmp_list = []
        tmp_list.append(book[i])
    if i == N - 1:
        tmp_list.sort(key=lambda x: -x[1])
        for j in tmp_list:
            print(j[2])
'''

n = int(input())
rest = []
for i in range(n):
    s_, p_ = input().split()
    p_ = int(p_)
    rest.append([s_, p_, i + 1])

rest.sort(key=lambda x: x[1], reverse=True)
print(rest)
rest.sort(key=lambda x: x[0])
print(rest)
for i in range(n):
    print(rest[i][2])