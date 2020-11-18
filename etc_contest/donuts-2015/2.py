N, M = map(int, input().split())
A = list(map(int, input().split()))
dp = [[0] * N for _ in range(2 ** N + 1)]
ans = 0
people_set = []
for _ in range(M):
    bonus = list(map(int, input().split()))
    point = bonus.pop(0)
    cnt = bonus.pop(0)
    people_set.append([point, cnt, set(bonus)])
print(people_set)

for i in range(2 ** N):
    now_people = set()
    unit_cnt = 0
    tmp_ans = 0
    # ユニット自体の基礎能力値
    for j in range(N):
        if (i >> j) & 1:
            dp[i][j] += A[j]
            now_people.add(j + 1)
            unit_cnt += 1
    if unit_cnt != 9:
        continue
    for now in people_set:
        point, cnt, bonus_people_set = now[0], now[1], now[2]
        if len(bonus_people_set & now_people) == cnt:
            tmp_ans += point
    tmp_ans = sum(dp[i])
    ans = max(ans, tmp_ans)

for row in dp:
    print(row)

print(ans)