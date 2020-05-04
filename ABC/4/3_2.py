N = int(input())
N %= 30
cards = list(range(1, 7))
for i in range(N):
    cards[i % 5], cards[i % 5 + 1] = cards[i % 5 + 1], cards[i % 5]
print(*cards, sep="")