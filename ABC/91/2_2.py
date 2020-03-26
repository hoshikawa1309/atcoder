from collections import Counter
N = int(input())
blue_cards = Counter(input() for _ in range(N))
M = int(input())
red_cards = Counter(input() for _ in range(M))
ans = 0
for blue_word, blue_count in blue_cards.items():
    tmp_ans = blue_count
    if blue_word in red_cards.keys():
        tmp_ans -= red_cards[blue_word]
    if tmp_ans > ans:
        ans = tmp_ans
print(ans)

