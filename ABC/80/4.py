N = int(input())
A = list(map(int,input().split()))
cnt2 = 0
cnt4 = 0
for a in A:
    if a % 4 == 0:
        cnt4 += 1
    elif a % 2 == 0:
        cnt2 += 1
N -= max(cnt2 - 1 , 0)
print("Yes" if N // 2 <= cnt4 else "No")