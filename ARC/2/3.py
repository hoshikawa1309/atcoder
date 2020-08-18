N = int(input())
command = input()
keys = ['A', 'B', 'X', 'Y']
short_cuts = []
for key1 in keys:
    for key2 in keys:
        short_cuts.append(key1 + key2)
ans = float('inf')
for i in range(len(short_cuts) - 1):
    for j in range(i + 1, len(short_cuts)):
        short_cut1 = short_cuts[i]
        short_cut2 = short_cuts[j]
        tmp_ans = 0
        now = 0
        while now < N - 1:
            c = command[now:now + 2]
            if c == short_cut1 or c == short_cut2:
                now += 2
            else:
                now += 1
            tmp_ans += 1
        if now == N - 1:
            tmp_ans += 1
        ans = min(tmp_ans, ans)
print(ans)
