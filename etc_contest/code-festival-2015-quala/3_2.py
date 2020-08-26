s = list(input())
K = int(input())
ans = []
for c in s:
    cnt = ord('z') - ord(c) + 1
    if c == 'a':
        ans.append('a')
    elif K >= cnt:
        K -= cnt
        ans.append('a')
    else:
        ans.append(c)
K %= 26
if 122 < ord(ans[-1]) + K:
    ans[-1] = chr(ord(ans[-1]) + K - 26)
else:
    ans[-1] = chr(ord(ans[-1]) + K)
print(*ans,sep='')
