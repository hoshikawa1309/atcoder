N = int(input())
A = list(map(int , input().split()))
lst = []
for idx , a in enumerate(A):
    lst.append([a,idx])
lst.sort()
for value in lst:
    print(value[1] + 1 , end = ' ')