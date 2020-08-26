s = input()
ans = float('inf')
for i in range(26):
    c = chr(ord('a') + i)
    work_s = s
    cnt = 0
    while len(set(work_s)) != 1:
        next_s = ''
        for i in range(len(work_s) - 1):
            if work_s[i] == c or work_s[i + 1] == c:
                next_s += c
            else:
                next_s += work_s[i]
        work_s = next_s
        cnt += 1
    if ans > cnt:
        ans = cnt

print(ans)