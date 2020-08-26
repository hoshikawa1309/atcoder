from collections import Counter
s = input()
Counter_s = Counter(s)
odd_cnt = 0
odd_key = 0
for key, val in Counter_s.items():
    if key != 'x' and val % 2 == 1:
        odd_cnt += 1
        odd_key = key
if len(Counter_s.items()):
    print(0)
    exit()
if odd_cnt > 1:
    print(-1)
    exit()


