N = int(input())
N -= 1
alphabets = []
for i in range(26):
    alphabets.append(chr(ord('a') + i))

idx = 1
while 26 ** idx <= N:
    idx += 1
ans = []
while idx > 1:
    ans.append(alphabets[N // (26 ** (idx - 1)) - 1])
    N %= 26 ** (idx - 1)
    idx -= 1
ans.append(alphabets[N])
print(*ans, sep='')
# 51まではOK,52の