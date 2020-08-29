N = int(input())
flags = [True] * 9
ans = 0
for _ in range(N):
    S = input()
    for i in range(9):
        if S[i] == 'x':
            flags[i] = True
            ans += 1
        elif S[i] == 'o':
            if flags[i]:
                ans += 1
                flags[i] = False
        else:
            flags[i] = True
print(ans)