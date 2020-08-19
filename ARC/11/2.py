d = {'b': 1, 'c': 1, 't': 3, 'j': 3, 'l': 5, 'v': 5, 'p': 7, 'm': 7, 'n': 9, 'g': 9, 'd': 2, 'w': 2, 'f': 4, 'q': 4, 's': 6, 'x': 6, 'h': 8, 'k': 8, 'z': 0, 'r': 0 }
N = int(input())
W = list(input().split())
keys = d.keys()
ans = []
for j in range(N):
    word = W[j]
    tmp_ans = ''
    for i in range(len(word)):
        target = word[i].lower()
        if target in keys:
            tmp_ans += str(d[target])
    if tmp_ans:
        ans.append(tmp_ans)
print(*ans, sep=' ')