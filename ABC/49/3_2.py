from collections import deque
S = input()
candidates = ['dream', 'dreamer', 'erase', 'eraser']
start = len(S)
end = len(S)
Flag = True
while start > 0:
    print(S[start:end])
    for s in candidates:
        len_s = len(s)
        now_start = start - len_s
        now_end = end
        if S[now_start:now_end] == s:
            start -= len_s
            end -= len_s
            break
    else:
        Flag = False
        break
if Flag and start < 0 and end <= 0:
    print('YES')
else:
    print('NO')