from collections import Counter

def cmb(n, r):
    return n * (n - 1) // r



N = int(input())
ball_com = [0] * (N + 1)
balls = list(map(int, input().split()))
balls_counter = Counter(balls)
for key, val in balls_counter.items():
    ball_com[key - 1] = cmb(val, 2)

cmb_sum = sum(ball_com)
for ball in balls:
    print(cmb_sum - ball_com[ball - 1] + cmb(balls_counter[ball] - 1, 2))
