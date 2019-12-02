N = int(input())
cnt = 0
for i in range(1,N//2 + 1):
    if N - i != i:
        cnt += 1
print(cnt)