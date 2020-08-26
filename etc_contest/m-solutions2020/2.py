cards = list(map(int, input().split()))
K = int(input())
for i in range(K):
    if cards[0] >= cards[1]:
        cards[1] *= 2
    else:
        cards[2] *= 2
# print(cards)
if cards[0] < cards[1] < cards[2]:
    print('Yes')
else:
    print('No')
