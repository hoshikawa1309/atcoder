N = int(input())
s = input()
t = input()
idx = 0
for i in range(N):
    tmp_s = s[N - i - 1:]
    tmp_t = t[:i + 1]
    if tmp_s == tmp_t:
        idx = i + 1

print(len(s + t[idx:]))

