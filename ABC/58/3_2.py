from collections import Counter
N = int(input())
words = list(list(input()) for _ in range(N))
if N == 1:
    print(sorted(words[0]))
    exit()

word = Counter(words[0])
for i in range(1, N):
    now_word = Counter(words[i])
print(sorted(list(word)))