N = int(input())
p = list(map(int , input().split()))
sorted_p = sorted(p)
count = 0
for i in range(N):
    if p[i] != sorted_p[i]:
        count += 1
if count <= 2:
    print("YES")
else:
    print("NO")