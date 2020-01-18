N , K = map(int,input().split())
R , S , P = map(int,input().split())
T = list(input())
is_get_list = [True] * K
ans = 0


for i in range(K , N):
    now = T[i]
    before = T[i - K]
    if now == before and is_get_list[i - K]:
        is_get_list.extend([False])
    else:
        is_get_list.extend([True])
# print(is_get_list)
for i in range(N):
    if not is_get_list[i]:
        continue
    if T[i] == 'r':
        ans += P
    if T[i] == 's':
        ans += R
    if T[i] == 'p':
        ans += S
print(ans)