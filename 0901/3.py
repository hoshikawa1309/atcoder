N = int(input())
height = list(map(int, input().split()))
max = 0
count = 0
tmp = 0
while count < len(height) - 1:
    corrent = height[count]
    if height[count + 1] <= corrent:
        tmp += 1
    else:
        tmp = 0
    if max < tmp:
        max = tmp
    count += 1
print(max)
