from collections import Counter
N = int(input())
BlueCard = list(input() for _ in range(N))
M = int(input())
RedCard = list(input() for _ in range(M))
BlueCard_Counter = Counter(BlueCard)
RedCard_Counter = Counter(RedCard)
ans = 0
for key , blue_cnt in BlueCard_Counter.items():
    if key in RedCard:
        red_cnt = RedCard_Counter[key]
    else:
        red_cnt = 0
    now = blue_cnt - red_cnt
    if ans < now:
        ans = now
print(ans)
