A, B = map(int,input().split())
for i in range(10 ** 6 + 1):
    if i * 8 // 100 == A and i // 10 == B:
        print(i)
        exit()
print("-1")