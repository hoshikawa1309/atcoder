N = int(input())
H = list(map(int,input().split()))
cnt = 1
height = H[0]
for val in H[1:]:
    if height <= val:
        cnt += 1
        height = val
print(cnt)