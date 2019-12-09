N = int(input())
s = []
Flag = True
for _ in range(N):
    p = int(input())
    s.append(p)
    if p % 10 != 0:
        Flag = False
if Flag:
    print("0")
    exit()

ans = sum(s)
if ans % 10 != 0:
    print(ans)
    exit()
else:
    s.sort()
    for val in s:
        if val % 10 == 0:
            continue
        ans -= val
        print(ans)
        exit()