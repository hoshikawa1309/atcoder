N = int(input())
a = list(map(int,input().split()))
ave = sum(a) / len(a)
ave = round(ave)
#print(ave)
ans = 0
for val in a:
    ans += (val - ave) ** 2
print(ans)