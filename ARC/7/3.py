pattern = list(input())
len_pattern = len(pattern)
for i in range(len_pattern):
    if pattern[i] == 'o':
        pattern[i] = True
    else:
        pattern[i] = False
if all(pattern):
    print('1')
    exit()
ans = float('inf')
while not pattern[0]:
    tmp = pattern.pop(0)
    pattern.append(tmp)
for _ in range(len_pattern):
    for tv_num in range(2, len_pattern + 1):
        is_ok = True
        for end in range(1, len_pattern + 1):
            start = max(end - tv_num, 0)
            if not any(pattern[start:end]):
                is_ok = False
                break
        if is_ok:
            ans = min(ans, tv_num)
    tmp = pattern.pop(0)
    pattern.append(tmp)
print(ans)


