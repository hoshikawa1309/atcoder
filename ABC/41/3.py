N = int(input())
a = list(map(int,input().split()))
s = []
for i in range(N):
    s.append([a[i],i + 1])
s.sort(reverse=True)
for val in s:
    print(val[1])