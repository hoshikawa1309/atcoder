N = int(input())
max = 0
h_list = list(map(int , input().split()))
for i in h_list:
    if max < i:
        max = i
    elif max - 1 > i:
        print("No")
        exit(0)
print("Yes")
