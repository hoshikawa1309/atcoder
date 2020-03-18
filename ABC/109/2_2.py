N = int(input())
words = [input() for _ in range(N)]
set_words = list(set(words))
if len(set_words) != N:
    print("No")
    exit()

now_word = words[0]

for i in range(1, N):
    if now_word[-1] != words[i][0]:
        print("No")
        exit()
    now_word = words[i]
print("Yes")