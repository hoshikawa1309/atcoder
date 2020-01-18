S = list(input())
K = int(input())
cnt = 0
start = S[0]
for i in range(len(S)):
    if start != S[i]:
        break
    if i == len(S) - 1:
        print(len(S) * K // 2)
        exit()
ans = 0
now = start
for i in range(len(S)):
    if i == len(S) - 1:
        if now == S[i]:
            cnt += 1
        ans += cnt // 2
    else:
        if S[i] != now :
            ans += cnt // 2
            cnt = 1
            now = S[i]
        else:
            cnt += 1

end = S[-1]
start_cnt = 0
end_cnt = 0
for c in S:
    if c == start:
        start_cnt += 1
    else:
        break
for i in range(len(S) - 1 , - 1, -1):
    if S[i] == end:
        end_cnt += 1
    else:
        break
add = 0
if end_cnt % 2 == 1 and start_cnt % 2 == 1 and start == end:
    add = (K - 1)
print(ans * K + add)