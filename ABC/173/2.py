judge = ['AC', 'WA', 'TLE', 'RE']
cnt = [0] * 4
N = int(input())
for _ in range(N):
    s = input()
    for i in range(len(judge)):
        if s == judge[i]:
            cnt[i] += 1
for i in range(4):
    print(judge[i] + ' ' + 'x' + ' ' + str(cnt[i]))
