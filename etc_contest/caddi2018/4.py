N = int(input())
A = [int(input()) for _ in range(N)]
for a in A:
    if a % 2 != 0:
        print('first')
        exit()
print('second')