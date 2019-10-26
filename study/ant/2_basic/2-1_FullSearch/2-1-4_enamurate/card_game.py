import itertools
import math
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
win_cnt = 0
for a in itertools.permutations(A , N):
    for b in itertools.permutations(B , N):
        a_victory = 0
        b_victory = 0
        for i in range(N):
            if a[i] > b[i]:
                a_victory += 1
            elif a[i] < b[i]:
                b_victory += 1
        if a_victory > b_victory:
            win_cnt += 1



print(win_cnt / math.factorial(N) ** 2)