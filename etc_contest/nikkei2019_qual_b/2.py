from collections import Counter
N = int(input())
A = list(input())
B = list(input())
C = list(input())

ans = 0
for c in zip(A, B, C):
    char_cnt = Counter(c)
    max_val = 0
    for val in char_cnt.values():
        if val > max_val:
            max_val = val
    ans += 3 - max_val

print(ans)