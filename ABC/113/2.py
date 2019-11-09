N = int(input())
t , x = map(int,input().split())
h_list = list(map(int,input().split()))
tmp = []
for h in h_list:
    tmp1 = abs(x - (t - h * 0.006))
    tmp.append(tmp1)
print(tmp.index(min(tmp)) + 1)