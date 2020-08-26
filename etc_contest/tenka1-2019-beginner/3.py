N = int(input())
S = input()
black_cnt = 0
white_cnt = 0
for i in range(N):
    if S[i] == '#':
        black_cnt += 1
    else:
        white_cnt += 1
ans = min(black_cnt, white_cnt)
tmp_ans = white_cnt
for i in range(N):
    if S[i] == '#':
        tmp_ans += 1
    else:
        tmp_ans -= 1
    ans = min(ans, tmp_ans)
print(ans)