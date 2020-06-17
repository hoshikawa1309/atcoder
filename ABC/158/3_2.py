A, B = map(int, input().split())
for ans in range(1, 1001):
    tmp_A = ans * 8 // 100
    tmp_B = ans // 10
    if tmp_A == A and tmp_B == B:
        print(ans)
        exit()
print('-1')