A, B = map(int, input().split())
if B == 1:
    print("0")
    exit()
now = A
cnt = 1
while now < B:
    now += (A - 1)
    cnt += 1
print(cnt)