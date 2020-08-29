N, A, B, C, D = map(int, input().split())
S = input()
for i in range(A - 1, max(C, D) - 1):
    if S[i] == S[i + 1] == '#':
        print("No")
        exit()

if C < D:
    print("Yes")
else:
    for i in range(B - 2, D - 1):
        if S[i:i + 3] == '...':
            print("Yes")
            exit()
    print('No')
