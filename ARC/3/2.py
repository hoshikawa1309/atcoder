N = int(input())
words = [input()[::-1] for _ in range(N)]
words.sort()
for word in words:
    print(word[::-1])