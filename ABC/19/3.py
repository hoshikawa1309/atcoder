N = int(input())
a = list(map(int,input().split()))
for i in range(len(a)):
    while (a[i] / 2).is_integer():
        a[i] //= 2
print(len(set(a)))