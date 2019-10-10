N , Q = map(int,input().split())
S = list(input())
slice_list = []
for _ in range(Q):
    l , r =map(int,input().split())
    slice_list.append([l - 1,r - 1])
cnt_list = [0] * (N + 1)

for i in range(N - 1):
    if S[i] == "A" and S[i + 1] == "C":
        cnt_list[i + 1] = cnt_list[i] + 1
    else:
        cnt_list[i + 1] = cnt_list[i]

for i in range(Q):

    print(cnt_list[slice_list[i][1]] - cnt_list[slice_list[i][0]])