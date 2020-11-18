N, M = map(int, input().split())
A = list(map(int, input().split()))
dp = [0] * (2 ** N + 1)
ans = 0
bonus_set = []
for _ in range(M):
    bonus = list(map(int, input().split()))
    point = bonus.pop(0)
    cnt = bonus.pop(0)
    bonus_set.append([point, cnt, set(bonus)])


for i in range(2 ** N):
    now_people = set()
    unit_cnt = 0
    tmp_ans = 0
    # ユニット自体の基礎能力値
    for j in range(N):
        if (i >> j) & 1:
            tmp_ans += A[j]
            now_people.add(j + 1)
            unit_cnt += 1
    if unit_cnt != 9:
        continue
    for bonus in bonus_set:
        bonus_point, cnt, people = bonus
        if len(people & now_people) >= 3:
            tmp_ans += bonus_point
    dp[i] = tmp_ans
    ans = max(tmp_ans, ans)
print(ans)
