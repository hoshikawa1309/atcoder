N = int(input())
c1 = 0
c2 = 0
c3 = 0
ans = 0
for _ in range(N):
    s = input()
    for i in range(len(s) - 1):
        if s[i:i + 2] == 'AB':
            ans += 1
    if s[0] == 'B' and s[-1] == 'A':
        c3 += 1
    elif s[0] == 'B':
        c2 += 1
    elif s[-1] == 'A':
        c1 += 1


if c3 == 0:
    ans += min(c1, c2)
elif c1 == c2 == 0:
    ans += c3 - 1
elif c1 == 0 or c2 == 0:
    ans += c3
else:
    ans += min(c1, c2) + c3
print(ans)